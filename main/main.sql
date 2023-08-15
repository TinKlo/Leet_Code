# Write your MySQL query statement beloW
SELECT name AS Employee FROM 
(
	SELECT
		t1.id
		, t1.name as name
		, t1.salary 
		, t1.managerId
		, t2.salary as managar_salary 
	FROM Employee t1
	LEFT JOIN Employee t2 ON t1.managerId = t2.id 
	WHERE t1.salary > t2.salary
	) AS  raw WHERE salary > managar_salary
