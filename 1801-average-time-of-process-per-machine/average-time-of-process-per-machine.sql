# Write your MySQL query statement below

select a1.machine_id, round(
    (select AVG(a1.timestamp) from Activity a1 where a1.activity_type='end' and a1.machine_id  = a2.machine_id)-
    (select AVG(a2.timestamp) from Activity a2 where a2.activity_type='start' and a1.machine_id = a2.machine_id),3
) as processing_time
from Activity a1 join Activity a2
on a1.machine_id = a2.machine_id
group by a1.machine_id