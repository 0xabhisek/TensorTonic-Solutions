-- Write your SQL query here
select segment_name, metric_name
from segments cross join metrics
order by segment_name, metric_name