"""dbt model generation prompt templates."""

DBT_MODEL_GENERATION_PROMPT = """You are an expert dbt model generator. Create a dbt model based on the provided schema.

Schema:
{schema}

Table Name: {table_name}
Model Type: {model_type}

Please generate:
1. **dbt Model SQL**: A complete dbt model SQL file
2. **dbt Model YAML**: The corresponding model configuration YAML
3. **Documentation**: Comments explaining the model logic
4. **Tests**: Suggested dbt tests for data quality

Requirements:
- Follow dbt best practices
- Include proper documentation
- Add appropriate tests
- Use meaningful column names
- Include data type transformations
- Add incremental logic if appropriate

Format your response as:

## dbt Model SQL
```sql
-- models/{model_name}.sql
[Generated SQL]
```

## dbt Model YAML
```yaml
-- models/{model_name}.yml
[Generated YAML]
```

## Documentation
[Model documentation and logic explanation]

## Suggested Tests
[Data quality test recommendations]
"""

DBT_SCHEMA_ANALYSIS_PROMPT = """You are an expert dbt schema analyst. Analyze the provided schema and suggest the best dbt model structure.

Schema:
{schema}

Please provide:
1. **Model Type Recommendation**: Should this be a staging, intermediate, or mart model?
2. **Column Transformations**: What transformations should be applied?
3. **Data Types**: What data types should be used?
4. **Naming Conventions**: How should columns be renamed?
5. **Business Logic**: What business rules should be applied?
6. **Dependencies**: What other models might this depend on?

Focus on:
- dbt best practices
- Data quality considerations
- Performance optimization
- Maintainability
- Business value
"""
