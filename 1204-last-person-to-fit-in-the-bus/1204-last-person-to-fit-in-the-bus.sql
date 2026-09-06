# Write your MySQL query statement below
select person_name
from (
    select person_name,turn,SUM(weight) OVER(ORDER BY turn ) AS total_weight
    from queue
) t
where total_weight<=1000
order by turn desc
limit 1;