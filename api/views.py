# api/views.py
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Session, Message
from .langchain_logic import process_message    # cspell: disable-line
from django.views.decorators.csrf import csrf_exempt
from langchain.schema import HumanMessage, AIMessage    # cspell: disable-line
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token  # cspell: disable-line
from rest_framework.authentication import TokenAuthentication

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated access
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        # Log the user in
        login(request, user)
        
        # Retrieve or create a token for the authenticated user
        token, created = Token.objects.get_or_create(user=user)
        
        # Return the token and user info in the response
        return Response({
            'status': 'success',
            'user_id': user.id,
            'token': token.key  # Send the token to the frontend
        })
    
    # If authentication failed
    return Response({'status': 'error', 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'status': 'success'})

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated access
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'status': 'success', 'user_id': user.id}, status=201)
    return Response(serializer.errors, status=400)
# ---

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure only authenticated users can create a session
def create_session(request):
    # Associate the session with the currently authenticated user
    session = Session.objects.create(user=request.user)
    return Response({'session_id': session.id}, status=201)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_session(request, session_id):
    try:
        session = Session.objects.get(id=session_id, user=request.user)
        messages = Message.objects.filter(session=session).values('id', 'text', 'timestamp', 'from_user')
        return JsonResponse({'session_id': session.id, 'messages': list(messages)}, status=200)
    except Session.DoesNotExist:
        return JsonResponse({'error': 'Session not found'}, status=404)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])  # Specify TokenAuthentication
@permission_classes([IsAuthenticated])
def get_sessions(request):
    if request.user.is_authenticated:
        sessions = request.user.sessions.all().values('id', 'created_at')
        return JsonResponse({'sessions': list(sessions)}, status=200)
    else:
        return JsonResponse({'error': 'Authentication required'}, status=401)

@csrf_exempt
def messages(request, session_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message_text = data['text']
            tip_of_tongue = data.get('tipOfTongue', False)  # Retrieve the flag
            session = Session.objects.get(id=session_id)
        except (json.JSONDecodeError, KeyError, Session.DoesNotExist) as e:
            return JsonResponse({'error': 'Invalid request or session not found'}, status=400)

        # Save user message
        user_message = Message.objects.create(session=session, text=message_text, from_user=True)

        # Retrieve conversation history
        conversation_messages = Message.objects.filter(session=session).order_by('timestamp')

        # Construct the conversation history for the LLM
        conversation = []
        for msg in conversation_messages:
            if msg.from_user:
                conversation.append(HumanMessage(content=msg.text))
            else:
                conversation.append(AIMessage(content=msg.text))

        # Process the message with LangChain, passing the conversation history and the flag
        response_text = process_message(conversation, tip_of_tongue=tip_of_tongue)

        # Save system response
        assistant_message = Message.objects.create(session=session, text=response_text, from_user=False)

        return JsonResponse({'message': response_text}, status=200)

    elif request.method == 'GET':
        messages = Message.objects.filter(session_id=session_id).values('id', 'text', 'timestamp', 'from_user')
        return JsonResponse({'messages': list(messages)}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  # Require authentication
def delete_session(request, session_id):
    try:
        session = Session.objects.get(id=session_id)
        session.delete()  # This will also delete all messages associated with the session due to the CASCADE delete
        return JsonResponse({'message': 'Session deleted successfully'}, status=204)
    except Session.DoesNotExist:
        return JsonResponse({'error': 'Session not found'}, status=404)