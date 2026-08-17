# Write your MySQL query statement below
SELECT e.name AS Employee
FROM employee e
INNER JOIN employee m
ON e.managerID=m.iD
WHERE e.salary>m.salary;