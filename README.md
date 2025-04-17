# About

SurfBuddy is a full-stack web application which recommends surfboards based on skill level, height, and weight. It utilizes a RESTful API and an external LLM to provide personalized suggestions.

# Overview

Still in progress

# General Idea of the Communication and Data Flow:

### User Request - Frontend (Vue.js):

A user initiates a request on the frontend within the Chatfield, surfboard recommendation based on the provided information e.g. weight, height, skill.

### Request Handling - Django Backend:

Django receives the user request and processes it, parsing the request data to extract relevant information to initiate the recommendation process.

### Logical Layer Module (LLM):

The LLM, which encapsulates the recommendation logic and algorithms, receives the parsed request data from Django to generate personalized recommendations based on user preferences and historical interactions.

### Recommendation Generation - LLM to Django:

Once the LLM processes the request and generates recommendations using AI algorithms, it sends the recommended items back to Django, encapsulated in a response structure.

### Data Retrieval - Django to Database:

Django, upon receiving the recommendation results from the LLM, fetches additional data from the database, such as product details or content information related to the recommendations.

### Response Construction - Django to Frontend:

Django assembles the recommendation results along with the retrieved data from the database into a structured response, which is then sent back to the frontend (Vue.js) to display the personalized recommendations to the user.

# Project Setup

Quick run through of how to setup the project for local development

## Frontend

1. Create a virtual environment for the frontend by using "venv" or "conda"

```
conda create -n surfbuddy-frontend
conda activate surfbuddy-frontend
```

2. Navigate to the frontend directory and install dependecies

```
cd frontend
npm install
```

3. Run the Development Server

```
npm run dev
```

## Backend

Still in progress
