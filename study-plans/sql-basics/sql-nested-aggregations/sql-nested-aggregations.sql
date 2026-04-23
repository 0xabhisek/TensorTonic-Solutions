-- Write your SQL query here
with cte1 as (select order_date, sum(amount) as date_amt, count(id) as date_cnt 
    from orders
group by order_date)

select  sum(date_cnt)/count(order_date) as avg_daily_orders, avg(date_amt) as avg_daily_revenue, max(date_cnt) as busiest_day_orders 
    from cte1;