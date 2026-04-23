-- Write your SQL query here
select e.name, salary, dept_name
from employees e inner join departments d 
on e.dept_id = d.id 
order by e.name 