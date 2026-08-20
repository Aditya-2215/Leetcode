# Write your MySQL query statement below
SELECT class
FROM courses
Group by class
having count(student)>=5;