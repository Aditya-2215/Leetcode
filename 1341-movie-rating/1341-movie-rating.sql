# Write your MySQL query statement below
(
    select u.name AS results
from users u
join movierating mr
on u.user_id=mr.user_id
group by u.user_id ,u.name
order by count(*) desc , u.name
limit 1
)

union all

(
    select m.title AS results
from movies m
join movierating AS mr
on m.movie_id=mr.movie_id
where mr.created_at>='2020-02-01'
and mr.created_at<'2020-03-01'
group by m.movie_id,m.title
order by AVG(mr.rating) desc , m.title
limit 1
);