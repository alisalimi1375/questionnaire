# Questionnaire API

## Overview

The **Questionnaire API** is a RESTful API developed using Python, Django, and Django Rest Framework (DRF). This API provides functionality for managing questionnaires, questions, and answers, along with user management. 

The API supports different types of questions and answers, with flexible validation mechanisms powered by a polymorphic structure.

---

## Features

- Create, retrieve, update, and delete (CRUD) operations for **Questionnaires**, **Questions**, **Answers**, and **Users**.
- Supports multiple types of questions and answers, each validated using polymorphic validators.
- User management functionality.

---

## Technology Stack

- **Python** 
- **Django** - Web framework
- **Django Rest Framework (DRF)** - For building APIs

---

## Django Apps

The project is structured with two primary Django apps:

1. **`questionnaires`**:
   - Manages all questionnaire-related operations including questions and answers.
   - Contains models for:
     - `Questionnaire`
     - `Question`
     - `Answer`
     - Validators for the `details` field that handle different question/answer types.
   - Validators reside in `questionnaires.validators` and handle types from `questionnaires.qa_types`.

2. **`users`**:
   - Handles user management, including creation and management of users.

---

## Models and Resources

The API exposes the following resources:

1. **Questionnaire**: Represents a set of questions.
2. **Question**: Represents an individual question within a questionnaire.
3. **Answer**: Represents an answer to a specific question within a questionnaire.
4. **User**: Represents a user of the system.

---

## Endpoints

The API provides the following endpoints:

### Questionnaire Endpoints
- `GET /questionnaires/` - List all questionnaires.
- `POST /questionnaires/` - Create a new questionnaire.
- `GET /questionnaires/<questionnaire_id>/` - Retrieve a specific questionnaire.
- `PUT /questionnaires/<questionnaire_id>/` - Update a specific questionnaire.
- `DELETE /questionnaires/<questionnaire_id>/` - Delete a specific questionnaire.

### Question Endpoints
- `GET /questionnaires/<questionnaire_id>/questions/` - List all questions in a questionnaire.
- `POST /questionnaires/<questionnaire_id>/questions/` - Add a new question to a questionnaire.
- `GET /questionnaires/<questionnaire_id>/questions/<question_id>/` - Retrieve a specific question.
- `PUT /questionnaires/<questionnaire_id>/questions/<question_id>/` - Update a specific question.
- `DELETE /questionnaires/<questionnaire_id>/questions/<question_id>/` - Delete a specific question.

### Answer Endpoints
- `GET /questionnaires/<questionnaire_id>/questions/<question_id>/answers/` - List all answers to a question.
- `POST /questionnaires/<questionnaire_id>/questions/<question_id>/answers/` - Submit an answer to a question.
- `GET /questionnaires/<questionnaire_id>/questions/<question_id>/answers/<answer_id>/` - Retrieve a specific answer.
- `PUT /questionnaires/<questionnaire_id>/questions/<question_id>/answers/<answer_id>/` - Update a specific answer.
- `DELETE /questionnaires/<questionnaire_id>/questions/<question_id>/answers/<answer_id>/` - Delete a specific answer.

### User Endpoints
- `GET /users/` - List all users.
- `POST /users/` - Create a new user.
- `GET /users/<user_id>/` - Retrieve a specific user.
- `PUT /users/<user_id>/` - Update a specific user.
- `DELETE /users/<user_id>/` - Delete a specific user.

---

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd questionnaire-api
