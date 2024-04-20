# Write your MySQL query statement below

select e.employee_id,e.name,count(*) as 'reports_count', round (avg(f.age)) as 'average_age' from 
Employees e 
join Employees f
on e.employee_id=f.reports_to
group by e.employee_id
order by e.employee_id