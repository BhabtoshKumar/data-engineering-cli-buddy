-- fct_customer_activity.sql
-- Customer activity fact table for Customer360 analytics

WITH customer_events AS (
    SELECT 
        customer_id,
        event_timestamp,
        event_type,
        event_properties,
        source_system,
        -- Extract additional properties
        JSON_EXTRACT(event_properties, '$.product_id') as product_id,
        JSON_EXTRACT(event_properties, '$.category') as category,
        JSON_EXTRACT(event_properties, '$.amount') as amount,
        JSON_EXTRACT(event_properties, '$.page_url') as page_url,
        JSON_EXTRACT(event_properties, '$.session_id') as session_id
    FROM {{ ref('stg_customer_events') }}
    WHERE customer_id IS NOT NULL
),

daily_activity AS (
    SELECT 
        customer_id,
        DATE(event_timestamp) as activity_date,
        event_type,
        COUNT(*) as event_count,
        COUNT(DISTINCT session_id) as session_count,
        SUM(CAST(COALESCE(amount, 0) AS DECIMAL(10,2))) as total_amount,
        COUNT(DISTINCT product_id) as unique_products,
        COUNT(DISTINCT category) as unique_categories,
        -- Session duration (simplified)
        MAX(event_timestamp) - MIN(event_timestamp) as session_duration_seconds,
        -- First and last events of the day
        MIN(event_timestamp) as first_event_time,
        MAX(event_timestamp) as last_event_time
    FROM customer_events
    GROUP BY customer_id, DATE(event_timestamp), event_type
),

customer_dim AS (
    SELECT 
        customer_id,
        customer_segment,
        value_segment,
        activity_level
    FROM {{ ref('dim_customer') }}
),

final_activity AS (
    SELECT 
        da.customer_id,
        da.activity_date,
        da.event_type,
        da.event_count,
        da.session_count,
        da.total_amount,
        da.unique_products,
        da.unique_categories,
        da.session_duration_seconds,
        da.first_event_time,
        da.last_event_time,
        cd.customer_segment,
        cd.value_segment,
        cd.activity_level,
        -- Additional calculated fields
        CASE 
            WHEN da.total_amount > 0 THEN 'revenue_generating'
            ELSE 'non_revenue'
        END as activity_type,
        CASE 
            WHEN da.session_count > 5 THEN 'high_engagement'
            WHEN da.session_count > 2 THEN 'medium_engagement'
            ELSE 'low_engagement'
        END as engagement_level,
        -- Day of week for analysis
        DAYOFWEEK(da.activity_date) as day_of_week,
        -- Month for trend analysis
        MONTH(da.activity_date) as month,
        -- Year for trend analysis
        YEAR(da.activity_date) as year
    FROM daily_activity da
    LEFT JOIN customer_dim cd ON da.customer_id = cd.customer_id
)

SELECT 
    customer_id,
    activity_date,
    event_type,
    event_count,
    session_count,
    total_amount,
    unique_products,
    unique_categories,
    session_duration_seconds,
    first_event_time,
    last_event_time,
    customer_segment,
    value_segment,
    activity_level,
    activity_type,
    engagement_level,
    day_of_week,
    month,
    year,
    -- Metadata
    CURRENT_TIMESTAMP() as created_at,
    'customer360_etl' as source_system
FROM final_activity
