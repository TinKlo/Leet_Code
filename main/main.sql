# Write your MySQL query statement below
select name as Employee from 
(
select t1.id, t1.name as name, t1.salary , t1.managerId, t2.salary as managar_salary from Employee t1
left join Employee t2 on t1.managerId = t2.id 
where t1.salary > t2.salary
) as raw where salary > managar_salary
