"""SQL optimization prompt templates."""

SQL_OPTIMIZATION_PROMPT = """You are an expert SQL optimizer and data engineer. Analyze the following SQL query and provide optimization suggestions.

SQL Query:
{sql_query}

Please provide:
1. **Performance Analysis**: Identify potential performance bottlenecks
2. **Optimization Suggestions**: Specific improvements with explanations
3. **Optimized Query**: A rewritten version of the query
4. **Index Recommendations**: Suggest indexes that could help
5. **Best Practices**: Any SQL best practices that should be applied

Focus on:
- Query execution plan optimization
- Index usage
- CTE simplification
- Column pruning
- Join optimization
- Subquery optimization

Format your response as:
## Performance Analysis
[Your analysis]

## Optimization Suggestions
[Your suggestions]

## Optimized Query
```sql
[Optimized SQL]
```

## Index Recommendations
[Index suggestions]

## Best Practices
[Best practices applied]
"""

SQL_EXPLAIN_PROMPT = """You are an expert SQL analyst. Explain what the following SQL query does in simple terms.

SQL Query:
{sql_query}

Please provide:
1. **Purpose**: What is this query trying to accomplish?
2. **Logic Flow**: Step-by-step explanation of the query logic
3. **Key Components**: Important parts (joins, filters, aggregations)
4. **Data Sources**: What tables/views are being used
5. **Output**: What kind of data will be returned

Keep the explanation clear and accessible to data engineers.
"""
