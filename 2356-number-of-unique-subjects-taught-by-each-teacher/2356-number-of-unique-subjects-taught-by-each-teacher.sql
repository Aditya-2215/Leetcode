/* Write your PL/SQL query statement below */
SELECT teacher_id ,COUNT(Distinct(subject_id)) AS cnt
From teacher
Group by teacher_id;