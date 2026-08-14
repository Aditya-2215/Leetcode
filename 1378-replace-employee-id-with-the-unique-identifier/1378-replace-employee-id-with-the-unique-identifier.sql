/* Write your PL/SQL query statement below */
Select eu.unique_id ,e.name
From employees e
LEFT JOIN employeeUNI eu
ON eu.id=e.id;