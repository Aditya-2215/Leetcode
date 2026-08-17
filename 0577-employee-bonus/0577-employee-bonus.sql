/* Write your PL/SQL query statement below */
SELECT e.name,b.bonus
from employee e
LEFT JOIN  bonus b
ON e.empId=b.empId
WHERE b.bonus<1000 
OR b.bonus IS NULL;