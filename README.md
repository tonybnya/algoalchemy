# AlgoAlchemy

A clever mix of Data Structures and Algorithms (DSA) and the magic (alchemy) of Python, implemented with Flask.

## Project Structure

This project contains an API implementation using Python Flask:

```
./algochemy/
├── README.md
├── algoalchemy.db
├── api
│   ├── app
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── models
│   │   └── routes
│   ├── pyproject.toml
│   ├── run.py
│   ├── tests
│   │   ├── conftest.py
│   │   ├── test_ping.py
│   │   └── test_root.py
│   └── uv.lock
├── dsa
│   └── linked_list.py
└── dummy_data.py
```

## Purpose

This project demonstrates how to implement a real-world API using Flask, then implement some data structures and algorithms in a project.
This approach avoid the usual habit of learning data structures and algorithms out of context.

## Getting Started

### Setting Up the Environment

This project uses `uv` for dependency management and virtual environments. If you don't have `uv` installed, you can install it following the instructions at [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv).

```bash
# At the root of the project, create and activate a virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Change to the api directory
cd api

# Install all dependencies from pyproject.toml
uv sync --active
```

This will create a virtual environment, install all the dependencies specified in the `pyproject.toml` file, and create/update the `uv.lock` file with the exact versions used.

### Running the Flask Implementation

```bash
# Make sure the virtual environment is activated and you're in the api directory
python3 run.py
# or
uv run --active flask --app run:app run
```

The Flask API will be available at `http://localhost:5000`.

### Database

This implementation uses a SQLite database file located at the project root.

To populate the database with sample data, use the `dummy_data.py` script:

```bash
# Make sure the virtual environment is activated and you're in the api directory
python3 dummy_data.py
```

The script will create sample users and blog posts in the database.

### Managing Dependencies

If you need to add or update dependencies, you can modify the `pyproject.toml` file and then run:

```bash
# Sync dependencies with your environment
uv sync --active
```

To verify installed packages in your environment:

```bash
# List all installed packages
uv pip list
```

### API Documentation

<!-- TODO -->

## Running Tests

The project has a test suite located in the `./api/tests` directory.

```bash
# Make sure the virtual environment is activated
cd api
pytest
```
