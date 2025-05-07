# AlgoAlchemy

A clever mix of algorithms and the magic (alchemy) of Python, implemented with Flask.

## Project Structure

This project contains an API implementation using Python Flask:

```
./algoalchemy/
├── api/                # Flask implementation
│   ├── app/            # Flask application code
│   ├── dummy_data.py   # Data generation script
│   ├── run.py          # Flask entry point
│   └── pyproject.toml  # Flask dependencies
├── dsa/                # Data structures and algorithms
└── tests/              # Test suite
```

## Purpose

This project demonstrates how to implement a real-world API using Flask, then implement some data structures and algorithms in a project.
This approach avoid the usual habit of learning data structures and algorithms out of context.

## Getting Started

### Setting Up the Environment

The project uses a virtual environment to isolate the dependencies:

```bash
# At the root of the project
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install all dependencies (both Flask and FastAPI)
pip3 install -r requirements.txt
```

### Running the Flask Implementation

```bash
# Make sure the virtual environment is activated
cd flask
python run.py
```

The Flask API will be available at `http://localhost:5000`.

### Database

This implementation uses a SQLite database file located at the project root.

To populate the database with sample data, use the `dummy_data.py` script:

```bash
# Populate the database for the Flask implementation
python dummy_data.py flask

```

### API Documentation

- Flask: No built-in documentation
  TODO

## Running Tests

Each implementation has its own test suite located in its respective `tests` directory.

### Running Flask Tests

```bash
# Make sure the virtual environment is activated
cd flask
pytest tests/
```

### Running All Tests

To run tests for both implementations:

```bash
# From the project root
pytest api/tests/
```
