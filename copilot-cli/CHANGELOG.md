# Changelog

All notable changes to the Data Engineering CLI Copilot will be documented in this file.

## [0.1.0] - 2024-01-XX

### Added
- Initial project structure and CLI framework
- Typer-based CLI with command registry
- Ollama integration with LangChain
- Prompt template system for different use cases
- File utility functions for parsing SQL, YAML, JSON, and Python files
- Mock Customer360 data pipeline for testing
- Basic test framework with pytest
- Comprehensive documentation and README

### CLI Commands
- `copilot sql optimize <query.sql>` - SQL optimization (placeholder)
- `copilot dag explain <dag.py>` - DAG explanation (placeholder)
- `copilot dbt generate --schema <schema.yaml>` - dbt model generation (placeholder)
- `copilot schema compare --expected <exp.json> --actual <act.json>` - Schema comparison (placeholder)
- `copilot setup` - Setup guide and environment configuration

### Architecture
- **CLI Framework**: Typer for type-safe CLI development
- **LLM Integration**: Ollama client with fallback model support
- **File Parsing**: Support for SQL, YAML, JSON, and Python files
- **Prompt Templates**: Structured prompts for each command type
- **Mock Pipeline**: Complete Customer360 ETL pipeline for testing

### Mock Data Pipeline
- Airflow DAG: `customer360_etl.py` with 10 tasks
- dbt Models: `dim_customer.sql` and `fct_customer_activity.sql`
- Schemas: Customer events and CRM export schemas
- Sample Queries: Top customers analysis query

### Development Setup
- Project metadata in `pyproject.toml`
- Dependencies in `requirements.txt`
- Environment configuration template
- Basic test suite
- Code formatting with Black and isort

### Next Steps (M2-M8)
- [ ] Implement SQL optimization with LLM integration
- [ ] Implement DAG explanation with Python AST parsing
- [ ] Implement dbt model generation from schemas
- [ ] Implement schema comparison and drift detection
- [ ] Add comprehensive unit tests
- [ ] Add integration tests with mocked LLM responses
- [ ] Polish CLI output with Rich formatting
- [ ] Make package installable via pip

### Technical Decisions
- **CLI Framework**: Typer chosen for type safety and modern Python support
- **LLM Provider**: Ollama for local, open-source LLM hosting
- **Fallback Strategy**: Automatic fallback to alternative models
- **File Formats**: Support for common data engineering file types
- **Testing**: pytest with mocked LLM responses for CI/CD

### Known Issues
- All main commands are currently placeholders
- LLM integration needs Ollama to be running locally
- No error handling for LLM connection issues
- Limited file validation and error messages

---

## [Unreleased]

### Planned Features
- SQL query optimization with performance analysis
- Airflow DAG parsing and natural language explanation
- dbt model generation from JSON/YAML schemas
- Schema drift detection and comparison
- Rich terminal output with tables and formatting
- Comprehensive error handling and validation
- Integration tests with sample data
- Documentation and examples
