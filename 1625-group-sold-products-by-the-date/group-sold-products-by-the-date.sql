# Write your MySQL query statement below

select sell_date, count(distinct(product)) as num_sold, group_concat(Distinct(product)) as products
from Activities
group by sell_date