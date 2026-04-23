-- Write your SQL query here
select name, city
, coalesce(sum(amount),0) as total_spent
from customers c 
left join orders o 
on c.id = o.customer_id
group by c.id, name, city 
order by total_spent desc, name;