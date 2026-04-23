-- Write your SQL query here
select username, experiment_name, variant, revenue
from 
(select u.username, u.id, e.experiment_name, e.variant
from users u join experiment_assignments e 
on u.id = e.user_id) t
join conversions c 
on t.id = c.id 
order by experiment_name, revenue desc, username
