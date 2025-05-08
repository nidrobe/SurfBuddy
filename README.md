# About

SurfBuddy is a full-stack web application which recommends surfboards based on skill level, height, and weight. It utilizes a RESTful API and an external LLM to provide personalized suggestions. As a Learning Project, this serves as a platform for exploring AI-based recommendation systems.

# Overview

<img src="frontend/src/assets/Overview.png" width="600" height="350">

# General Idea of the Communication Flow:

## Phase 1: LLM Only (Currently in Development)

1. Frontend requests to Django.
2. Django passes data to the LLM.
3. LLM generates recommendations and sends them back to Django.
4. Django formats the response and sends it to the frontend for display.

5. Validate if the LLM can provide reasonable recommendations in the first place before moving on to phase two.

## Phase 2: Database Integration

Enhance the LLM-driven recommendations with detailed information retrieved from a database, providing a richer and more informative user experience e.g. surfboard pictures, price tags etc.

# Project Setup

Quick run through of how to setup the project for local development

## Frontend

1. Ensure Node.js and npm are installed

- Check Node.js version: `node -v`
- Check npm version: `npm -v`
- If not installed, download and install Node.js from https://nodejs.org/

2. Create a virtual environment for the frontend by using "venv" or "conda"

```
conda create -n frontend
conda activate frontend
```

3. Navigate to the frontend directory and install dependecies

```
cd frontend
npm install
```

4. Run the development server

```
npm run dev
```

The Vue.js development server should be now running at `http://localhost:5173/`.

## Backend

1. Create a virtual environment for the backend by using "venv" or "conda"

```
conda create -n backend
conda activate backend
```

2. Navigate to the backend directory and install dependecies

```
cd backend
pip install -r requirements.txt
```

3. Create a .env file within the backend directory and insert your OpenAI API key. Make sure to have enough credit on your OpenAI Account.

```
OPENAI_API_KEY="your-api-key"
```

5. Apply database migrations

```
python manage.py makemigrations
python manage.py migrate
```

5. Start the Server

```
python manage.py runserver
```

The Django development server should be now running at `http://127.0.0.1:8000/` or `http://localhost:8000/`.

# OpenAI API

The OpenAI API is fundamentally stateless. Each API request is treated as an independent event. The API doesn't automatically retain information from previous interactions or "remember" anything about past conversations (see screenshot below). Therefore to create a chat experience with a sense of memory using the OpenAI API, a memory system has to be engineered. This invloves storing the conversation in some external storage and retrieving the relevant parts of conversation history.

## Memory System (Currently in Development)

...
