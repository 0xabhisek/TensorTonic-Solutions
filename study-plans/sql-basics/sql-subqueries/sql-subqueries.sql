-- Write your SQL query here


SELECT name, price, (price - (SELECT AVG(price) FROM products)) as vs_avg
FROM products 
WHERE id IN (SELECT product_id FROM sales)
ORDER BY vs_avg desc, name

