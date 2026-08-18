# Write your MySQL query statement below
SELECT e.name
FROM employee AS e
INNER JOIN Employee AS m 
ON e.id=m.managerID
GROUP BY m.managerID
HAVING COUNT(m.managerId)>=5;