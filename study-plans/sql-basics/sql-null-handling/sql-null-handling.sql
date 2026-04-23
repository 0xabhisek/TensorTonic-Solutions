-- Write your SQL query here
select name, COALESCE(email, 'N/A') as display_email,
    (case when deactivated_at IS NULL then 'active' else 'inactive' end) as status
from customers
    where phone is not null
order by name