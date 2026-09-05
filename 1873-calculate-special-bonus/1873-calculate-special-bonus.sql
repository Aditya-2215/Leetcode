# Write your MySQL query statement below
select employee_id,
CASE
    WHEN employee_id%2=1
    AND name NOT LIKE 'M%'
    THEN Salary
    ELSE 0
    END AS bonus
    from employees
order by employee_id;