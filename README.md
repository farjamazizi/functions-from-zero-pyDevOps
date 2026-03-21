# Functions From Zero: Python DevOps Toolkit

`functions-from-zero-pyDevOps` is a small Python project that combines simple utility modules, command-line tools, and a FastAPI service into one learning-focused DevOps sandbox.

The project currently covers three practical areas:

- Calculator utilities with a CLI for basic arithmetic
- Logistics helpers for city coordinates and route distance calculations
- Wikipedia search and summary endpoints exposed through an API

It is designed as a hands-on repository for practicing Python packaging, testing, linting, formatting, containerization, and lightweight service development.

## Project Highlights

- `FastAPI` app with logistics and Wikipedia endpoints
- `Click`-based CLIs for calculator and logistics workflows
- `pytest` test suite for core functions and API behavior
- `Dockerfile` for containerized execution
- `Makefile` for install, test, lint, and format tasks

## Project Structure

```text
.
├── main.py              # FastAPI application
├── calCLI.py            # Calculator CLI
├── logisticsCLI.py      # Logistics CLI
├── mylib/
│   ├── calc.py          # Math helpers
│   ├── logistics.py     # Coordinate and distance helpers
│   └── wiki.py          # Wikipedia integration helpers
├── test_project.py      # Calculator and CLI tests
├── test_logistics.py    # Logistics and API tests
├── Dockerfile           # Container setup
└── Makefile             # Common development commands
```

## Features

### 1. Calculator CLI

Run basic arithmetic operations from the terminal:

```bash
python calCLI.py add 2 3
python calCLI.py sub 5 1
python calCLI.py mul 4 6
python calCLI.py div 8 2
python calCLI.py pow 2 4
```

### 2. Logistics Tools

Work with a predefined list of major U.S. cities:

- Find coordinates for a city
- Calculate distance between two cities
- Calculate total route distance across multiple cities

Examples:

```bash
python logisticsCLI.py coordinate Chicago
python logisticsCLI.py distance "New York" Chicago
python logisticsCLI.py total-distance "New York" Chicago Seattle
```

### 3. FastAPI Service

Start the API locally:

```bash
uvicorn main:app --reload
```

Available endpoints:

- `GET /`
- `POST /coordinate`
- `POST /distance`
- `POST /total-distance`
- `POST /wiki/search`
- `POST /wiki/summary`
- `POST /wiki/url`

Example request:

```bash
curl -X POST http://127.0.0.1:8000/distance \
  -H "Content-Type: application/json" \
  -d '{"city1":"New York","city2":"Chicago"}'
```

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Or use the `Makefile`:

```bash
make install
make lint
make test
make format
```

## Docker

Build and run the service in a container:

```bash
docker build -t functions-from-zero .
docker run -p 8080:8080 functions-from-zero
```

Then open `http://127.0.0.1:8080`.

## Why This Project

This repository is a practical starter for learning how application code, testing, APIs, CLIs, and deployment basics fit together in a Python DevOps workflow. It stays intentionally small, which makes it easier to extend and refactor.

## Roadmap

### Near Term

- Improve naming consistency and fix spelling issues such as `distanse`
- Expand supported cities beyond the current hardcoded list
- Add input validation and clearer API error messages
- Add README badges and example API responses

### Mid Term

- Add CI with GitHub Actions for linting, tests, and Docker builds
- Introduce coverage thresholds and stricter quality gates
- Add typed function signatures across the codebase
- Improve test coverage for Wikipedia helpers and CLI edge cases

### Longer Term

- Replace hardcoded city data with a structured dataset or external source
- Add route planning features such as travel time and multi-stop optimization
- Package the CLIs for easier installation
- Deploy the API to a cloud platform with environment-based configuration

## Current Status

The project already has a working base:

- core Python modules
- CLI tools
- a containerized FastAPI app
- automated tests

The next step is to improve polish, consistency, and automation so it feels more like a production-ready service rather than a learning prototype.
