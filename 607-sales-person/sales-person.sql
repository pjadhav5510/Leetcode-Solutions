# Write your MySQL query statement below

select s.name
from SalesPerson s
where s.name not in  (select s.name 
    from SalesPerson s join Orders o
    on s.sales_id = o.sales_id
    join Company c
    on o.com_id = c.com_id
    where c.name = 'Red') 