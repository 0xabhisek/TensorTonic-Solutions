-- Write your SQL query here
SELECT month, revenue,
       LAG(revenue, 1, 0) OVER (ORDER BY month, id) AS prev_revenue,
       revenue - LAG(revenue, 1, 0) OVER (ORDER BY month, id) AS revenue_change
FROM monthly_revenue
ORDER BY month ASC, id ASC;
