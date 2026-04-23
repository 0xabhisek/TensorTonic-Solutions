-- Write your SQL query here
WITH cte AS 
    (SELECT customer, COUNT(id) AS order_count, SUM(amount) AS total_spent 
    FROM orders
    GROUP BY customer
    ORDER BY total_spent desc, customer)

SELECT *
from cte where order_count > 1
