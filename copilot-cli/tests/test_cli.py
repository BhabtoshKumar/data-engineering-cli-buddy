"""Tests for CLI functionality."""

import pytest
from typer.testing import CliRunner

from copilot_cli.cli.main import app


@pytest.fixture
def runner():
    """Create a CLI runner for testing."""
    return CliRunner()


def test_cli_help(runner):
    """Test that CLI help works."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Data Engineering CLI Copilot" in result.stdout


def test_cli_version(runner):
    """Test that CLI version works."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "Data Engineering Copilot v" in result.stdout


def test_sql_command_help(runner):
    """Test SQL command help."""
    result = runner.invoke(app, ["sql", "--help"])
    assert result.exit_code == 0
    assert "Optimize SQL queries" in result.stdout


def test_dag_command_help(runner):
    """Test DAG command help."""
    result = runner.invoke(app, ["dag", "--help"])
    assert result.exit_code == 0
    assert "Explain Airflow DAGs" in result.stdout


def test_dbt_command_help(runner):
    """Test dbt command help."""
    result = runner.invoke(app, ["dbt", "--help"])
    assert result.exit_code == 0
    assert "Generate dbt models" in result.stdout


def test_schema_command_help(runner):
    """Test schema command help."""
    result = runner.invoke(app, ["schema", "--help"])
    assert result.exit_code == 0
    assert "Compare schemas" in result.stdout


def test_setup_command(runner):
    """Test setup command."""
    result = runner.invoke(app, ["setup"])
    assert result.exit_code == 0
    assert "Data Engineering Copilot Setup" in result.stdout


def test_sql_command_with_nonexistent_file(runner):
    """Test SQL command with non-existent file."""
    result = runner.invoke(app, ["sql", "nonexistent.sql"])
    assert result.exit_code != 0  # Should fail


def test_dag_command_with_nonexistent_file(runner):
    """Test DAG command with non-existent file."""
    result = runner.invoke(app, ["dag", "nonexistent.py"])
    assert result.exit_code != 0  # Should fail
