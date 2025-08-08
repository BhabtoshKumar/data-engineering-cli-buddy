"""Main CLI entry point for the Data Engineering Copilot."""

import os
import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel

from copilot_cli import __version__

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

app = typer.Typer(
    name="copilot",
    help="🤖 Data Engineering CLI Copilot - AI-powered assistant for data engineers",
    add_completion=False,
    rich_markup_mode="rich",
)

console = Console()


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"[bold blue]Data Engineering Copilot v{__version__}[/bold blue]")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", callback=version_callback, help="Show version and exit"
    ),
    debug: bool = typer.Option(False, "--debug", help="Enable debug mode"),
) -> None:
    """🤖 Data Engineering CLI Copilot - AI-powered assistant for data engineers.
    
    Powered by local LLMs via Ollama, this tool helps data engineers with:
    • SQL optimization and analysis
    • Airflow DAG explanation and debugging
    • dbt model generation from schemas
    • Schema drift detection and comparison
    """
    if debug:
        os.environ["COPILOT_LOG_LEVEL"] = "DEBUG"
        console.print("[yellow]Debug mode enabled[/yellow]")


@app.command()
def sql(
    optimize: str = typer.Argument(..., help="SQL file to optimize"),
    output: str = typer.Option("rich", "--output", "-o", help="Output format (rich/json)"),
) -> None:
    """Optimize SQL queries using AI analysis."""
    console.print(f"[green]SQL optimization for: {optimize}[/green]")
    # TODO: Implement SQL optimization
    console.print("[yellow]SQL optimization feature coming soon![/yellow]")


@app.command()
def dag(
    explain: str = typer.Argument(..., help="Airflow DAG file to explain"),
    output: str = typer.Option("rich", "--output", "-o", help="Output format (rich/json)"),
) -> None:
    """Explain Airflow DAGs using AI analysis."""
    console.print(f"[green]DAG explanation for: {explain}[/green]")
    # TODO: Implement DAG explanation
    console.print("[yellow]DAG explanation feature coming soon![/yellow]")


@app.command()
def dbt(
    generate: str = typer.Argument(..., help="Schema file to generate dbt model from"),
    save: bool = typer.Option(False, "--save", "-s", help="Save generated files"),
    output: str = typer.Option("rich", "--output", "-o", help="Output format (rich/json)"),
) -> None:
    """Generate dbt models from schema files."""
    console.print(f"[green]dbt generation for: {generate}[/green]")
    # TODO: Implement dbt generation
    console.print("[yellow]dbt generation feature coming soon![/yellow]")


@app.command()
def schema(
    compare: str = typer.Argument(..., help="Expected schema file"),
    actual: str = typer.Argument(..., help="Actual schema file"),
    output: str = typer.Option("rich", "--output", "-o", help="Output format (rich/json)"),
) -> None:
    """Compare schemas and detect drift."""
    console.print(f"[green]Schema comparison: {compare} vs {actual}[/green]")
    # TODO: Implement schema comparison
    console.print("[yellow]Schema comparison feature coming soon![/yellow]")


@app.command()
def setup() -> None:
    """Setup the copilot environment and dependencies."""
    console.print(Panel.fit(
        "[bold blue]Data Engineering Copilot Setup[/bold blue]\n\n"
        "1. Install Ollama: https://ollama.ai\n"
        "2. Pull required models:\n"
        "   • ollama pull codellama:7b\n"
        "   • ollama pull mistral:7b\n"
        "3. Copy env.example to .env and configure\n"
        "4. Run: pip install -e .\n\n"
        "[green]Ready to use![/green]",
        title="Setup Guide"
    ))


if __name__ == "__main__":
    app()
