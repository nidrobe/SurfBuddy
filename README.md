# About

SurfBuddy is a full-stack web application which recommends surfboards based on skill level, height, and weight. It utilizes a RESTful API and an external LLM to provide personalized suggestions. But Instead of relying on a web-based search, SurfBuddy leverages a dedicated database for surfboard information. As a Learning Project, this serves as a platform for exploring AI-based recommendation systems.

# Overview

<img src="frontend/src/assets/Overview.png" width="600" height="300">

# General Idea of the Communication and Data Flow:

### User Request - Frontend:

A user initiates a request on the frontend within the Chatfield, surfboard recommendation based on the provided information e.g. weight, height, skill.

### Request Handling - Django Backend:

Django receives the user request and processes it, parsing the request data to extract relevant information to initiate the recommendation process.

### Django to Large Language Model (LLM):

Instead of relying on predefined rules, Django sends the parsed data to the LLM. The LLM uses its internal logic to generate surfboard recommendations based on the received data.

### LLM to Django:

Once the LLM processes the request and generates recommendations, it sends the recommended items back to Django.

### Data Retrieval - Django to Database:

Receiving the recommendation results from the LLM, Django then may retrieve additional information from the database to enrich the recommendations (e.g., product details, images, etc.).

### Response Construction - Django to Frontend:

Django assembles the recommendation results along with the retrieved data from the database into a structured response, which is then sent back to the frontend to display the personalized recommendations to the user.

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

## Backend

Still in progress
