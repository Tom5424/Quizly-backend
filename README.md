# Quizly (backend)


## Table of Contents


1. [About the Project](#about-the-project)
2. [Technologies](#technologies)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [API Endpoints](#api-endpoints)


## About the Project
The Quizly backend is a robust REST API built with Django and Django REST Framework (DRF). It supports functionalities such as user registration, login, create, update and delete quizzes.
The quizzes will create with the gemini Ai.


## Technologies

- Python (Version 3.12.4)
- Django (Version 5.2.7)
- Django REST Framework (Version 3.16.1)
- yt-dlp (Version 2025.11.12)
- Whisper (Version 20250625)

  
## Prerequisites

  - Python
  - Django
  - Django REST Framework
  - pip
  - ffmpeg (install globally)
  - Whisper AI


## Installation


1 **Clone the repository:**
  ```
  git clone https://github.com/Tom5424/Quizly-backend.git .
  ```


2 **Create a virtual environment:**
  ```
  python -m venv env
  ```
  activate the virtual environment with ``` env\Scripts\activate ```


3 **Install dependencies:**
  ```
  pip install -r requirements.txt
  ```


4 **Create .env data with credentials and paste credentials with your own values:**

 ```
   GEMINI_API_KEY=your_api_key
 ```


5 **Start the Project:**
  ```
  py manage.py runserver
  ```


## API Endpoints


#### Authentification Endpoints:


- METHOD POST ``` api/register/ ``` Registers a new user

- METHOD POST ``` api/login/ ``` Login a user

- METHOD POST ``` api/token/refresh/ ``` Refresh the access token

- METHOD POST ``` api/logout/ ``` Logout the user and delete the access and refresh token


#### Quiz Enpoints:


 - METHOD POST ``` api/createQuiz/ ``` Creats a new quiz

 - METHOD GET ``` api/quizzes/ ``` Return a list of quizzes 

 - METHOD GET, PATCH, DELETE ``` api/quizzes/{quiz_id}/ ``` Retrieving, update or delete a single quiz
