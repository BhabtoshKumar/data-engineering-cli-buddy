"""File utility functions for the Data Engineering Copilot."""

import json
import sqlparse
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import ruamel.yaml
from rich.console import Console

console = Console()


def read_file(file_path: str) -> str:
    """Read a file and return its contents.
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        File contents as string
        
    Raises:
        FileNotFoundError: If file doesn't exist
        PermissionError: If file can't be read
    """
    try:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
            
    except Exception as e:
        console.print(f"[red]Error reading file {file_path}: {e}[/red]")
        raise


def parse_sql_file(file_path: str) -> str:
    """Parse and format a SQL file.
    
    Args:
        file_path: Path to the SQL file
        
    Returns:
        Formatted SQL content
    """
    content = read_file(file_path)
    
    # Parse and format SQL
    try:
        parsed = sqlparse.parse(content)
        formatted = sqlparse.format(
            content,
            reindent=True,
            keyword_case='upper',
            use_space_around_operators=True,
        )
        return formatted
    except Exception as e:
        console.print(f"[yellow]Warning: Could not parse SQL file {file_path}: {e}[/yellow]")
        return content


def parse_yaml_file(file_path: str) -> Dict[str, Any]:
    """Parse a YAML file.
    
    Args:
        file_path: Path to the YAML file
        
    Returns:
        Parsed YAML as dictionary
    """
    content = read_file(file_path)
    
    try:
        yaml = ruamel.yaml.YAML(typ='safe')
        return yaml.load(content)
    except Exception as e:
        console.print(f"[red]Error parsing YAML file {file_path}: {e}[/red]")
        raise


def parse_json_file(file_path: str) -> Dict[str, Any]:
    """Parse a JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Parsed JSON as dictionary
    """
    content = read_file(file_path)
    
    try:
        return json.loads(content)
    except Exception as e:
        console.print(f"[red]Error parsing JSON file {file_path}: {e}[/red]")
        raise


def parse_python_file(file_path: str) -> str:
    """Parse a Python file and extract DAG-related code.
    
    Args:
        file_path: Path to the Python file
        
    Returns:
        Python file content
    """
    content = read_file(file_path)
    
    # Basic validation that it's a Python file
    if not file_path.endswith('.py'):
        console.print(f"[yellow]Warning: File {file_path} doesn't have .py extension[/yellow]")
    
    return content


def save_file(content: str, file_path: str) -> None:
    """Save content to a file.
    
    Args:
        content: Content to save
        file_path: Path where to save the file
    """
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        console.print(f"[green]Saved file: {file_path}[/green]")
        
    except Exception as e:
        console.print(f"[red]Error saving file {file_path}: {e}[/red]")
        raise


def get_file_extension(file_path: str) -> str:
    """Get the file extension.
    
    Args:
        file_path: Path to the file
        
    Returns:
        File extension (e.g., '.sql', '.py', '.json')
    """
    return Path(file_path).suffix.lower()


def validate_file_exists(file_path: str) -> bool:
    """Validate that a file exists.
    
    Args:
        file_path: Path to the file
        
    Returns:
        True if file exists
    """
    return Path(file_path).exists()


def list_files_in_directory(directory: str, extensions: Optional[List[str]] = None) -> List[str]:
    """List files in a directory with optional extension filtering.
    
    Args:
        directory: Directory to search
        extensions: List of extensions to filter by (e.g., ['.sql', '.py'])
        
    Returns:
        List of file paths
    """
    path = Path(directory)
    if not path.exists():
        return []
    
    files = []
    for file_path in path.rglob('*'):
        if file_path.is_file():
            if extensions is None or file_path.suffix.lower() in extensions:
                files.append(str(file_path))
    
    return files
