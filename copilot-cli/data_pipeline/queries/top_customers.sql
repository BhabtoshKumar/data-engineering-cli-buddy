-- Top Customers Analysis
-- This query identifies the highest-value customers based on multiple metrics

WITH customer_metrics AS (
    SELECT 
        c.customer_id,
        c.first_name,
        c.last_name,
        c.email,
        c.customer_segment,
        c.total_spend,
        c.estimated_lifetime_value,
        ca.total_events,
        ca.purchase_count,
        ca.active_days,
        ca.days_since_last_activity,
        -- Calculate engagement score
        (ca.total_events * 0.3) + (ca.purchase_count * 0.5) + (ca.active_days * 0.2) as engagement_score,
        -- Calculate value score
        (c.total_spend * 0.6) + (c.estimated_lifetime_value * 0.4) as value_score,
        -- Calculate recency score (lower is better)
        CASE 
            WHEN ca.days_since_last_activity <= 7 THEN 100
            WHEN ca.days_since_last_activity <= 30 THEN 75
            WHEN ca.days_since_last_activity <= 90 THEN 50
            ELSE 25
        END as recency_score
    FROM dim_customer c
    LEFT JOIN (
        SELECT 
            customer_id,
            SUM(event_count) as total_events,
            SUM(CASE WHEN event_type = 'purchase' THEN event_count ELSE 0 END) as purchase_count,
            COUNT(DISTINCT activity_date) as active_days,
            MAX(days_since_last_activity) as days_since_last_activity
        FROM fct_customer_activity
        GROUP BY customer_id
    ) ca ON c.customer_id = ca.customer_id
    WHERE c.customer_id IS NOT NULL
),

customer_ranking AS (
    SELECT 
        *,
        -- Overall score combining all metrics
        (engagement_score * 0.3) + (value_score * 0.4) + (recency_score * 0.3) as overall_score,
        -- Rank by different criteria
        ROW_NUMBER() OVER (ORDER BY total_spend DESC) as spend_rank,
        ROW_NUMBER() OVER (ORDER BY engagement_score DESC) as engagement_rank,
        ROW_NUMBER() OVER (ORDER BY purchase_count DESC) as purchase_rank,
        ROW_NUMBER() OVER (ORDER BY overall_score DESC) as overall_rank
    FROM customer_metrics
)

SELECT 
    customer_id,
    first_name,
    last_name,
    email,
    customer_segment,
    total_spend,
    estimated_lifetime_value,
    total_events,
    purchase_count,
    active_days,
    days_since_last_activity,
    engagement_score,
    value_score,
    recency_score,
    overall_score,
    spend_rank,
    engagement_rank,
    purchase_rank,
    overall_rank,
    -- Customer tier based on overall score
    CASE 
        WHEN overall_score >= 80 THEN 'Platinum'
        WHEN overall_score >= 60 THEN 'Gold'
        WHEN overall_score >= 40 THEN 'Silver'
        ELSE 'Bronze'
    END as customer_tier,
    -- Action recommendations
    CASE 
        WHEN days_since_last_activity > 90 THEN 'Re-engagement Campaign'
        WHEN purchase_count = 0 THEN 'First Purchase Incentive'
        WHEN total_spend < 100 THEN 'Upsell Opportunity'
        WHEN customer_segment = 'basic' AND overall_score > 60 THEN 'Segment Upgrade'
        ELSE 'Maintenance'
    END as recommended_action
FROM customer_ranking
WHERE overall_rank <= 100  -- Top 100 customers
ORDER BY overall_rank;
