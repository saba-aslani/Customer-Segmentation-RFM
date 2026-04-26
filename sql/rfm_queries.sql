-- 1. View all customer segments
SELECT *
FROM rfm_table
LIMIT 10;


-- 2. Count customers by segment
SELECT
    Segment,
    COUNT(*) AS customer_count
FROM rfm_table
GROUP BY Segment
ORDER BY customer_count DESC;


-- 3. Total revenue by segment
SELECT
    Segment,
    ROUND(SUM(Monetary), 2) AS total_revenue
FROM rfm_table
GROUP BY Segment
ORDER BY total_revenue DESC;


-- 4. Average RFM metrics by segment
SELECT
    Segment,
    ROUND(AVG(Recency), 2) AS avg_recency,
    ROUND(AVG(Frequency), 2) AS avg_frequency,
    ROUND(AVG(Monetary), 2) AS avg_monetary
FROM rfm_table
GROUP BY Segment
ORDER BY avg_monetary DESC;


-- 5. Top 10 customers by monetary value
SELECT
    customer_name,
    ROUND(Monetary, 2) AS total_spent,
    Frequency,
    Recency,
    Segment
FROM rfm_table
ORDER BY Monetary DESC
LIMIT 10;


-- 6. At-risk high-value customers
SELECT
    customer_name,
    Recency,
    Frequency,
    ROUND(Monetary, 2) AS total_spent,
    Segment
FROM rfm_table
WHERE Segment = 'At Risk'
ORDER BY Monetary DESC
LIMIT 10;