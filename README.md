## README.md

## API Layer Documentation

## Overview

This API layer provides a RESTful interface for managing user sessions, messages, and language model interactions.

## Endpoints

## Authentication

- `POST /login/`: Authenticate a user.
    

- `POST /logout/`: Log out the current user.
    

- `POST /register/`: Register a new user.
    

## Sessions

- `POST /sessions/`: Create a new session for the authenticated user.
    

- `GET /sessions/<session_id>/`: Retrieve a session by ID.
    

- `GET /sessions/`: List all sessions for the authenticated user.
    

- `DELETE /sessions/<session_id>/`: Delete a session.
    

## Messages

- `POST /messages/<session_id>/`: Send a message in a session.
    

- `GET /messages/<session_id>/`: Retrieve messages in a session.
    

## Models

## Session

- `id`: Unique session ID.
    

- `user`: Foreign key referencing the User model.
    

- `created_at`: Timestamp for session creation.
    

## Message

- `id`: Unique message ID.
    

- `session`: Foreign key referencing the Session model.
    

- `text`: Message text.
    

- `timestamp`: Timestamp for message creation.
    

- `from_user`: Boolean indicating if the message is from the user or the language model.
    

## Serializers

## RegisterSerializer

- `username`: Username for registration.
    

- `email`: Email for registration.
    

- `password`: Password for registration.
    

- `password2`: Password confirmation.
    

## UserSerializer

- `id`: User ID.
    

- `username`: Username.
    

- `email`: Email.
    

## Language Model Integration

The API uses the LangChain library to interact with the OpenAI language model.

## Requirements

- Django 4.2.16
    

- Django REST framework
    

- LangChain
    

- OpenAI API key
    

## Setup

- Install dependencies: `pip install -r requirements.txt`
    

- Set environment variables: `OPENAI_API_KEY`
    

- Run migrations: `python manage.py migrate`
    

- Start the server: `python manage.py runserver`