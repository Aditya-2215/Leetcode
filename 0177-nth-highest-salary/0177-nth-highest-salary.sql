CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select salary
from (select salary,DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk 
FROM employee) AS t
where rnk=N
LIMIT 1
  );
END