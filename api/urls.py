# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sessions/', views.create_session, name='create_session'),
    path('sessions/all/', views.get_sessions, name='get_sessions'),
    path('sessions/<int:session_id>/', views.get_session, name='get_session'),
    path('sessions/<int:session_id>/messages/', views.messages, name='messages'),  # Handles both GET and POST for messages
    # Delete Session
    path('sessions/<int:session_id>/delete/', views.delete_session, name='delete_session'),
    # Authentication paths
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    # Workflow-related endpoints
    path('save-workflow/<int:session_id>/', views.save_workflow, name='save_workflow'),
    path('get-workflow/<int:session_id>/', views.get_workflow, name='get_workflow'),
]
