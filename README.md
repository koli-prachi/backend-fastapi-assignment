# FastAPI Backend Assignment

## Overview

This project implements a **secure and scalable REST API** using **FastAPI**.

It includes:

- User Registration & Login
- JWT Authentication
- Role-Based Access Control (Admin/User)
- CRUD APIs for Tasks
- Secure password hashing
- API Documentation using Swagger
- Automated API testing using Pytest

---

# Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (JSON Web Tokens)
- Passlib (password hashing)
- Pytest
- Swagger UI

---

# Features

## Authentication

- Secure user registration
- Password hashing
- JWT token generation
- Login authentication

---

## Role-Based Access Control

Two roles are supported:

- **User**
- **Admin**

Admin-only routes are protected.

Example:

GET `/api/v1/users` → Admin only

---

# API Endpoints

## Register

POST `/api/v1/register`

Example Request

```
{
"name": "Prachi",
"email": "prachi@test.com",
"password": "123456"
}
```

---

## Login

POST `/api/v1/login`

Example Response

```
{
"token": "JWT_TOKEN"
}
```

---

# Task APIs (Protected)

Requires JWT token.

POST `/api/v1/tasks`
GET `/api/v1/tasks`

---

# Admin APIs

GET `/api/v1/users`

Only accessible to **admin users**.

---

# Running the Project

### Install dependencies

```
pip install -r requirements.txt
```

---

### Run server

```
python -m uvicorn backend.main:app --reload
```

---

### Open API documentation

```
http://127.0.0.1:8000/docs
```

---

# Running Tests

```
python -m pytest
```

---

# Scalability Notes

This system can be scaled using:

- PostgreSQL / MySQL
- Redis caching
- Docker containerization
- Microservices architecture
- Load balancing

---

# Author

Prachi Koli
Backend Developer Internship Assignment
