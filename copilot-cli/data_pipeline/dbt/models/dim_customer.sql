-- dim_customer.sql
-- Customer dimension table for Customer360 analytics

WITH customer_events AS (
    SELECT 
        customer_id,
        event_timestamp,
        event_type,
        event_properties,
        source_system
    FROM {{ ref('stg_customer_events') }}
    WHERE customer_id IS NOT NULL
),

customer_profile AS (
    SELECT 
        customer_id,
        first_name,
        last_name,
        email,
        phone,
        date_of_birth,
        registration_date,
        customer_segment,
        total_spend,
        last_purchase_date,
        source_system
    FROM {{ ref('stg_customer_profile') }}
    WHERE customer_id IS NOT NULL
),

customer_activity_summary AS (
    SELECT 
        customer_id,
        COUNT(*) as total_events,
        COUNT(DISTINCT DATE(event_timestamp)) as active_days,
        MIN(event_timestamp) as first_event_date,
        MAX(event_timestamp) as last_event_date,
        COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) as purchase_count,
        COUNT(CASE WHEN event_type = 'page_view' THEN 1 END) as page_view_count,
        COUNT(CASE WHEN event_type = 'cart_add' THEN 1 END) as cart_add_count
    FROM customer_events
    GROUP BY customer_id
)

SELECT 
    cp.customer_id,
    cp.first_name,
    cp.last_name,
    cp.email,
    cp.phone,
    cp.date_of_birth,
    cp.registration_date,
    cp.customer_segment,
    cp.total_spend,
    cp.last_purchase_date,
    cp.source_system,
    cas.total_events,
    cas.active_days,
    cas.first_event_date,
    cas.last_event_date,
    cas.purchase_count,
    cas.page_view_count,
    cas.cart_add_count,
    -- Calculated fields
    CASE 
        WHEN cas.total_events > 100 THEN 'high_activity'
        WHEN cas.total_events > 50 THEN 'medium_activity'
        ELSE 'low_activity'
    END as activity_level,
    CASE 
        WHEN cp.total_spend > 1000 THEN 'high_value'
        WHEN cp.total_spend > 500 THEN 'medium_value'
        ELSE 'low_value'
    END as value_segment,
    -- Days since last activity
    DATEDIFF('day', cas.last_event_date, CURRENT_DATE()) as days_since_last_activity,
    -- Customer lifetime value (simplified)
    COALESCE(cp.total_spend, 0) + (cas.total_events * 0.1) as estimated_lifetime_value
FROM customer_profile cp
LEFT JOIN customer_activity_summary cas ON cp.customer_id = cas.customer_id
WHERE cp.customer_id IS NOT NULL
