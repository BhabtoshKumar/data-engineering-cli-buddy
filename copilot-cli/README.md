# 🤖 Data Engineering CLI Copilot

A powerful CLI-based AI assistant for data engineers, powered by local LLMs via Ollama. Enhance your productivity with intelligent automation and deep understanding of data engineering artifacts.

## ✨ Features

- **SQL Optimization**: Analyze and optimize SQL queries with AI-powered suggestions
- **DAG Explanation**: Get natural language explanations of Airflow DAGs
- **dbt Model Generation**: Generate dbt models from schema definitions
- **Schema Drift Detection**: Compare schemas and identify drift issues
- **Local & Private**: Runs entirely on your machine with open-source LLMs

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama**: [https://ollama.ai](https://ollama.ai)
2. **Pull Required Models**:
   ```bash
   ollama pull codellama:7b
   ollama pull mistral:7b
   ```

### Installation

```bash
# Clone the repository
git clone https://github.com/data-engineering-copilot/cli.git
cd copilot-cli

# Install dependencies
pip install -e .

# Copy environment template
cp env.example .env
```

### Basic Usage

```bash
# SQL optimization
copilot sql optimize data_pipeline/queries/top_customers.sql

# DAG explanation
copilot dag explain data_pipeline/dags/customer360_etl.py

# dbt model generation
copilot dbt generate --schema data_pipeline/schemas/crm_export_schema.json --save

# Schema comparison
copilot schema compare --expected expected.json --actual actual.json
```

## 📋 Commands

### SQL Optimization
```bash
copilot sql optimize <query.sql> [--output rich|json]
```
Analyzes SQL queries and provides optimization suggestions including:
- Performance bottlenecks
- Index recommendations
- Query structure improvements
- Best practices

### DAG Explanation
```bash
copilot dag explain <dag.py> [--output rich|json]
```
Explains Airflow DAGs in natural language:
- Task dependencies and flow
- Schedule and retry configuration
- Data processing logic
- Potential issues and improvements

### dbt Model Generation
```bash
copilot dbt generate --schema <schema.yaml> [--save] [--output rich|json]
```
Generates dbt models from schema definitions:
- SQL model files
- YAML configuration
- Documentation
- Data quality tests

### Schema Comparison
```bash
copilot schema compare --expected <expected.json> --actual <actual.json> [--output rich|json]
```
Compares schemas and detects drift:
- Type changes
- Missing/extra fields
- Nullable constraint changes
- Impact assessment

## 🏗️ Architecture

```
copilot-cli/
├── copilot_cli/
│   ├── cli/           # Typer CLI framework
│   ├── llm/           # Ollama integration
│   └── utils/         # File parsing utilities
├── prompts/           # LLM prompt templates
├── data_pipeline/     # Mock Customer360 pipeline
├── examples/          # Sample files for testing
└── tests/            # Unit tests
```

## 🧪 Mock Pipeline: Customer360

The project includes a complete mock enterprise data pipeline:

- **Airflow DAG**: `data_pipeline/dags/customer360_etl.py`
- **dbt Models**: `data_pipeline/dbt/models/`
- **Schemas**: `data_pipeline/schemas/`
- **Sample Queries**: `data_pipeline/queries/`

Use these files to test the CLI features:

```bash
# Test SQL optimization
copilot sql optimize data_pipeline/queries/top_customers.sql

# Test DAG explanation
copilot dag explain data_pipeline/dags/customer360_etl.py

# Test dbt generation
copilot dbt generate --schema data_pipeline/schemas/crm_export_schema.json
```

## ⚙️ Configuration

Environment variables (set in `.env`):

```bash
# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=codellama:7b
OLLAMA_FALLBACK_MODEL=mistral:7b

# CLI Configuration
COPILOT_LOG_LEVEL=INFO
COPILOT_OUTPUT_FORMAT=rich
```

## 🧪 Testing

```bash
# Run unit tests
pytest tests/

# Run with coverage
pytest --cov=copilot_cli tests/

# Test CLI commands
copilot --help
copilot setup
```

## 🛠️ Development

### Project Structure
- **CLI Framework**: Typer for type-safe CLI development
- **LLM Integration**: LangChain + Ollama for local AI
- **File Parsing**: sqlparse, ruamel.yaml, jsonschema
- **Testing**: pytest with mocked LLM responses

### Adding New Features
1. Create command in `copilot_cli/cli/main.py`
2. Add prompt template in `prompts/`
3. Implement logic in appropriate module
4. Add tests in `tests/`

### Code Quality
```bash
# Format code
black copilot_cli/
isort copilot_cli/

# Lint code
flake8 copilot_cli/
mypy copilot_cli/
```

## 📚 Examples

### SQL Optimization
```sql
-- Input: Complex query with subqueries
SELECT 
    c.customer_id,
    c.first_name,
    COUNT(o.order_id) as order_count
FROM customers c
LEFT JOIN (
    SELECT customer_id, order_id 
    FROM orders 
    WHERE order_date >= '2024-01-01'
) o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name;
```

**Output**: Optimized query with CTEs, proper indexing, and performance improvements.

### DAG Explanation
```python
# Input: Airflow DAG with complex dependencies
dag = DAG('customer360_etl', schedule_interval='0 * * * *')
```

**Output**: Natural language explanation of the pipeline flow, dependencies, and scheduling.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) for local LLM hosting
- [LangChain](https://langchain.com) for LLM integration
- [Typer](https://typer.tiangolo.com) for CLI framework
- [Rich](https://rich.readthedocs.io) for beautiful terminal output

---

**Built with ❤️ for the data engineering community**
