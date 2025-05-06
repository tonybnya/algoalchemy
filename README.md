# AlgoAlchemy

A clever mix of algorithms and the magic (alchemy) of Python, implemented with both Flask and FastAPI.

## Project Structure

This project contains two identical API implementations using different Python web frameworks:

```
./algoalchemy/
├── flask/              # Flask implementation
│   ├── app/            # Flask application code
│   ├── dummy_data.py   # Data generation scripts
│   ├── run.py          # Flask entry point
│   └── pyproject.toml  # Flask dependencies
├── fastapi/            # FastAPI implementation
│   ├── app/            # FastAPI application code
│   ├── main.py         # FastAPI entry point
│   └── pyproject.toml  # FastAPI dependencies
├── dsa/                # Data structures and algorithms
└── tests/              # Test suite
```

## Purpose

This project demonstrates how to implement the same API functionality using two popular Python web frameworks:

- **Flask**: A lightweight WSGI web application framework
- **FastAPI**: A modern, fast web framework for building APIs with Python

By implementing the same endpoints in both frameworks, you can compare their approaches, performance, and development experience.

## Getting Started

### Setting Up the Environment

The project uses a shared virtual environment for both implementations:

```bash
# At the root of the project
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install all dependencies (both Flask and FastAPI)
pip install -e .

# Or, install only specific framework dependencies:
# For Flask only:
# pip install -e ".[flask]"
#
# For FastAPI only:
# pip install -e ".[fastapi]"
#
# For development tools (pytest, linting):
# pip install -e ".[dev]"
```

### Running the Flask Implementation

```bash
# Make sure the virtual environment is activated
cd flask
python run.py
```

The Flask API will be available at `http://localhost:5000`.

### Running the FastAPI Implementation

```bash
# Make sure the virtual environment is activated
cd fastapi
python -m uvicorn main:app --reload
```

The FastAPI API will be available at `http://localhost:8000`.

### Shared Database

Both implementations use the same SQLite database file located at the project root. This ensures data consistency when switching between frameworks.

To populate the database with sample data, use the `dummy_data.py` script:

```bash
# Populate the database for the Flask implementation
python dummy_data.py flask

# Populate the database for the FastAPI implementation
python dummy_data.py fastapi

# Populate the database for both implementations
python dummy_data.py both
```

Note: The FastAPI implementation currently has a placeholder for the data models. You'll need to implement those before the FastAPI data population will work.

### API Documentation

- Flask: No built-in documentation (consider adding Swagger UI)
- FastAPI: Interactive API documentation available at `http://localhost:8000/docs` or `http://localhost:8000/redoc`

## Running Tests

Each implementation has its own test suite located in its respective `tests` directory.

### Running Flask Tests

```bash
# Make sure the virtual environment is activated
cd flask
pytest tests/
```

### Running FastAPI Tests

```bash
# Make sure the virtual environment is activated
cd fastapi
pytest tests/
```

### Running All Tests

To run tests for both implementations:

```bash
# From the project root
pytest flask/tests/ fastapi/tests/
```
