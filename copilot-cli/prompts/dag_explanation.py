"""Airflow DAG explanation prompt templates."""

DAG_EXPLANATION_PROMPT = """You are an expert Airflow DAG analyst. Analyze the following Airflow DAG and provide a comprehensive explanation.

DAG Code:
{dag_code}

Please provide:
1. **DAG Overview**: What is the purpose of this DAG?
2. **Task Dependencies**: How are tasks connected and what's the execution flow?
3. **Schedule**: When does this DAG run?
4. **Retry Configuration**: What happens if tasks fail?
5. **Key Tasks**: What are the main operations being performed?
6. **Data Flow**: How does data move through this pipeline?
7. **Potential Issues**: Any potential problems or improvements?

Focus on:
- Task dependencies and execution order
- Retry and failure handling
- Data processing logic
- Performance considerations
- Monitoring and alerting

Format your response as:
## DAG Overview
[Purpose and high-level description]

## Task Dependencies
[Execution flow and dependencies]

## Schedule
[When the DAG runs]

## Retry Configuration
[Failure handling details]

## Key Tasks
[Main operations and their purposes]

## Data Flow
[How data moves through the pipeline]

## Potential Issues
[Problems or improvements to consider]
"""

DAG_DEBUG_PROMPT = """You are an expert Airflow DAG debugger. Analyze the following DAG for potential issues and provide debugging suggestions.

DAG Code:
{dag_code}

Please identify:
1. **Syntax Issues**: Any Python syntax problems
2. **Airflow Issues**: Incorrect Airflow operator usage
3. **Dependency Issues**: Problems with task dependencies
4. **Performance Issues**: Potential performance bottlenecks
5. **Best Practice Violations**: Airflow best practices not followed
6. **Security Issues**: Any security concerns
7. **Debugging Suggestions**: How to troubleshoot issues

Provide specific fixes and improvements.
"""
