"""Schema comparison prompt templates."""

SCHEMA_COMPARISON_PROMPT = """You are an expert data schema analyst. Compare the expected and actual schemas to identify drift and issues.

Expected Schema:
{expected_schema}

Actual Schema:
{actual_schema}

Please analyze:
1. **Schema Drift**: What differences exist between expected and actual?
2. **Type Changes**: Any data type modifications?
3. **Missing Fields**: Fields present in expected but not in actual?
4. **Extra Fields**: Fields in actual but not in expected?
5. **Nullable Changes**: Changes in nullability constraints?
6. **Impact Assessment**: What impact do these changes have?
7. **Recommendations**: How to handle the drift?

Focus on:
- Data type compatibility
- Field presence/absence
- Constraint changes
- Business impact
- Migration strategies

Format your response as:

## Schema Drift Summary
[High-level summary of differences]

## Detailed Analysis
### Type Changes
[Data type modifications]

### Missing Fields
[Fields in expected but not actual]

### Extra Fields
[Fields in actual but not expected]

### Nullable Changes
[Changes in nullability]

## Impact Assessment
[Business and technical impact]

## Recommendations
[How to handle the drift]
"""

SCHEMA_VALIDATION_PROMPT = """You are an expert data schema validator. Validate the provided schema for potential issues.

Schema:
{schema}

Please check for:
1. **Data Type Issues**: Inappropriate data types or constraints
2. **Naming Issues**: Poor naming conventions
3. **Missing Constraints**: Important constraints that should be added
4. **Performance Issues**: Schema design that could cause performance problems
5. **Security Issues**: Sensitive data handling concerns
6. **Best Practice Violations**: Schema design best practices not followed
7. **Improvement Suggestions**: How to improve the schema

Provide specific recommendations for each issue found.
"""
