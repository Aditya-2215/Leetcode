# Write your MySQL query statement below
SELECT employee_id 
FROM employees
where salary<30000
AND manager_id IS NOT NULL
and manager_id NOT IN(
    SELECT employee_id
    from employees

)
order by employee_id;