# Full-Stack Web Application

This is a full-stack web application developed using Django as the backend and Angular as the frontend. The application allows users to send and receive interest messages, accept or reject interests, and engage in real-time chat with other users.

## Table of Contents

- [Architecture and Design](#architecture-and-design)
- [Installation](#installation)
- [Backend (Django)](#backend-django)
- [Frontend (Angular)](#frontend-angular)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Architecture and Design

The application follows a client-server architecture, where the backend server is built with Django and the frontend client is built with Angular. Here is an overview of the architecture and design:

### Backend (Django)

The backend is responsible for handling user authentication, managing interest messages, and enabling real-time chat functionality. It consists of the following components:

- **Models**: The models define the structure of the database and include the User, Interest, and ChatMessage models.

- **Views**: The views handle incoming requests and perform CRUD operations on the data models.

- **URLs**: The URLs define the API endpoints and map them to the corresponding views.

- **Serializers**: The serializers convert the data models into JSON format for communication between the backend and frontend.

- **Authentication**: The backend uses Django Rest Framework's token authentication to handle user authentication.

- **Real-time Chat**: The backend uses Django Channels to enable real-time chat functionality through WebSockets.

### Frontend (Angular)

The frontend provides a user-friendly interface for interacting with the application. It includes components, services, routing, and state management. Here are the main components:

- **Components**: The components represent different parts of the application UI, such as login, registration, user list, interests, and chat.

- **Services**: The services handle API calls, authentication, and data management.

- **Routing**: The routing defines the navigation paths and maps them to the corresponding components.

- **State Management**: The state management uses Angular's ReactiveForms and RxJS to handle form data and asynchronous data streams.

## Installation

To run the application locally, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the backend directory: `cd backend`
3. Install Python dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Start the Django development server: `python manage.py runserver`

For the frontend:

1. Navigate to the frontend directory: `cd frontend`
2. Install Node.js dependencies: `npm install`
3. Start the Angular development server: `ng serve`

## Usage

Once the application is running, you can access it in your browser at `http://localhost:4200`. The application provides the following functionality:

- **User Authentication**: Users can register, log in, and log out of the application.

- **Sending and Receiving Interest Messages**: Users can send interest messages to other users and view received interest messages.

- **Accepting/Rejecting Interests**: Users can accept or reject interest messages received from other users.

- **Real-time Chat**: Users can engage in real-time chat with other users who have accepted their interests.

## Testing

Both the backend and frontend codebases have unit tests to ensure the correctness of the implemented features. To run the tests, follow these steps:

For the backend:

1. Navigate to the backend directory: `cd backend`
2. Run the tests: `python manage.py test`

For the frontend:

1. Navigate to the frontend directory: `cd frontend`
2. Run the tests: `ng test`

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
