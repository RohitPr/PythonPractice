with a as (select * from trips 
where client_id not in (select users_id from users where banned = 'yes')
and driver_id not in (select users_id from users where banned = 'yes')),

t2 as (select request_at,count(*) as ct from a left join users u
on a.client_id = u.users_id
where request_at between "2013-10-01" and "2013-10-03"
and status in ('cancelled_by_driver', 'cancelled_by_client')
group by 1),

t3 as (select request_at,count(*) as total from a left join users u
on a.client_id = u.users_id
where request_at between "2013-10-01" and "2013-10-03"
group by 1)

select t3.request_at as Day, round(ifnull(t2.ct/t3.total,0),2) as 'Cancellation Rate'
from t2 right join t3 using(request_at)