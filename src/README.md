# Pegatron Backend Hands-On

## Description

This project is a backend application developed as part of a hands-on exercise. It demonstrates key backend development concepts and practices.

## Features

- Create a user with “name” and “age” fields
- Delete a specific user by “name”
- Get a list of users who have been added
- Add multiple users from CSV file
- Calculate average age of each group of users

## Run on your local

1. Install Conda

   ```bash
   curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
   bash Miniconda3-latest-MacOSX-x86_64.sh

   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/hellowhaaa/Pegatron_backend_handson.git
   ```

3. Navigate to the project directory:
   ```bash
   cd pegatron_backend_handson
   ```
4. Install dependencies:
   ```bash
   conda create -n pegatron_backend_handson python=3.11
   source activate pegatron_backend_handson
   pip install -r requirements.txt
   ```
5. Activate application:
   ```bash
   uvicorn src.app:app --reload
   ```

## Run with Docker

### Build the Docker image

```bash
docker build -t user-age .
```

### Run the container

```bash
docker run -p 8000:8000 user-age
```

## Swagger

API and API doc are now available at:

- http://localhost:8000
- http://localhost:8000/docs

## Folder Structure

```
.
├── Dockerfile            # Docker config
├── app.db                # SQLite database
├── requirements.txt      # Python dependencies
└── src/
    ├── app.py            # App entry point
    ├── controllers/      # API routing
    ├── core/             # Config & DB setup
    ├── models/           # SQLAlchemy models
    ├── routes.py         # API route definitions
    ├── schemas/          # Pydantic schemas
    └── services/         # Service layer & Business logic
```

## Technologies Used

### 🧑‍💻 Language

- Python 3.11

### 📦 Packages

- pandas
- sqlite3 (built-in)

### 🐳 Tools

- Docker
