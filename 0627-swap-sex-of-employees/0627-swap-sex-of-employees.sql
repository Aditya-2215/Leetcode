/* Write your PL/SQL query statement below */
UPDATE SALARY
SET sex=CASE
when sex='m' then 'f'
when sex='f' then 'm'
end;
