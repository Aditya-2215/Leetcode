# Write your MySQL query statement below
select sell_date,COUNT(DISTINCT product) AS num_sold,
group_concat(DISTINCT product order by product separator ',') AS products
from activities
group by sell_date
order by sell_date;