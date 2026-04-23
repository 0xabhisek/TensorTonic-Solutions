-- Write your SQL query here
select
month, revenue,
(lag(revenue,1,0) over (order by month)) as prev_revenue,
(revenue - (lag(revenue,1,0) over (order by month))) as revenue_change
from monthly_revenue
order by month