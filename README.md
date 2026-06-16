# Fullstack Web App

A full-stack social interaction web application with a Django REST backend and an Angular frontend. The project focuses on user accounts, interest requests, and real-time chat between matched users.

## Features

- User registration, login, and logout
- Interest request flow between users
- Accept and reject actions for received interests
- Real-time chat for accepted connections
- REST API backend with Django and Django REST Framework
- Angular frontend for the user interface

## Tech Stack

- Backend: Django, Django REST Framework, Django Channels
- Frontend: Angular, RxJS, Reactive Forms
- Database: Django-supported relational database
- Realtime: WebSockets through Django Channels

## Project Structure

```text
backend/    Django API, models, serializers, views, routing, and websocket logic
frontend/   Angular application, components, services, routing, and forms
```

## Running Locally

Backend:

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Frontend:

```bash
cd frontend
npm install
ng serve
```

Open the frontend at `http://localhost:4200`.

## Testing

Backend:

```bash
cd backend
python manage.py test
```

Frontend:

```bash
cd frontend
ng test
```

## Notes

This project is a good candidate to keep public as a portfolio project. Useful next improvements would be screenshots, demo credentials, deployment notes, and a short architecture diagram.
