# Python Starter

This is a starter template for building powerful and extensible command-line interface (CLI) applications in Python. It comes with a set of modern tools and a modular structure to help you get started quickly.

## Features

-   **CLI Framework**: [Click](https://click.palletsprojects.com/) for creating beautiful and composable command-line interfaces.
-   **Package Management**: [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management and virtual environments.
-   **Asynchronous Support**: [asyncio](https://docs.python.org/3/library/asyncio.html) for building concurrent applications.
-   **Testing**: [pytest](https://docs.pytest.org/) for writing simple and scalable tests.
-   **Logging**: [loguru](https://loguru.readthedocs.io/en/stable/) for easy and powerful logging.
-   **Environment Variables**: [dotenv](https://github.com/theskumar/python-dotenv) for managing environment variables.
-   **Linting and Formatting**: [Ruff](https://github.com/astral-sh/ruff) for code formatting and linting.
-   **Type Checking**: [basedpyright](https://github.com/detachHead/basedpyright) for static type checking.

## Setup

1.  **Create a virtual environment and sync the uv dependencies:**

    ```bash
    uv sync
    ```

## Usage

This starter project includes a modular command structure where each command is its own file in the `cmd/` directory.

-   **Run a command:**

    To run the example `serve` command:

    ```bash
    python main.py serve --port=8080
    ```

-   **Get help for the CLI:**

    ```bash
    python main.py --help
    ```

    To get help for a specific command:

    ```bash
    python main.py serve --help
    ```

-   **Run tests:**

    ```bash
    uv run pytest
    ```

-   **Run linter and formatter:**

    ```bash
    uv run ruff check .
    uv run ruff format .
    ```

-   **Run type checker:**

    ```bash
    uv run basedpyright
    ```

## Extending the CLI

To add a new command to the CLI, simply create a new Python file in the `cmd/` directory. The file must contain a [Click command](https://click.palletsprojects.com/) named `cli`.

For example, to create a new command called `hello`, create a file named `cmd/hello.py` with the following content:

```python
import click

@click.command()
@click.argument('name')
def cli(name):
    """A simple command that greets you."""
    click.echo(f"Hello, {name}!")
```

The new `hello` command will be automatically discovered and available to the CLI.

You can then run your new command:

```bash
uv run main.py hello "World"
```
