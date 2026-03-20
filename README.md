# functions-from-zero-pyDevOps

This repository is an early-stage Python DevOps learning project focused on
building simple functions from scratch while practicing a basic development
workflow.

## Current Status

The project is still in a scaffold phase. It currently includes:

- A starter Python file in `hello.py` for simple function and debugging experiments
- A `requirements.txt` file with development and runtime dependencies
- A `Makefile` with commands for install, lint, test, format, and deploy
- A lightweight repository structure that can grow into a larger Python application

At the moment, this repo is more of a learning workspace than a finished
application.

## Tooling Included

The environment is set up with common Python development tools:

- `pytest` and `pytest-cov` for testing and coverage
- `pylint` for linting
- `black` for formatting
x = 1
y = 2
# import ipdb

# ipdb.set_trace()
print(x + y)

- `ipdb` for debugging

The dependency list also includes packages such as `click`, `fastapi`,
`uvicorn`, `wikipedia`, and `yake`, which gives the project room to expand into
CLI, API, or text-processing experiments.

## Development Commands

The `Makefile` currently provides these commands:

```bash
make install
make lint
make test
make format
make all
```

## Project Goal

The main goal of this repository is to learn by building: starting with simple
Python functions, then adding better structure, testing, automation, and
DevOps-friendly practices over time.
