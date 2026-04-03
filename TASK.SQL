SELECT
    DATA(event_time) as event_data,
    count(DISTINCT user_id) as dau

from events
group by event_data
order by event_data;
 
explain each one and what is it doing and why, what is DISTINCT 
it should be breaf and go through every line

SELECT DISTINCT user_id
from events
where event_type = 'login'
and user_id not in (
    SELECT user_id
    from events
    where event_type = 'purchase'
);


SELECT DISTINCT e.user_id
FROM events e
WHERE e.event_type = 'login'
AND NOT EXISTS (
    SELECT 1
    FROM events p
    WHERE p.user_id = e.user_id
    AND p.event_type = 'purchase'
);

what dose the e , p stands for and why use them and how they work 



SELECT DISTINCT p.user_id, date(p.event_time) as event_data
from events p 
where p.event_type = 'purchase'
and not exists(
    SELECT 1
    from events 1 
    where 1.user_id = p. user_id
    and 1.event_type = ' login'
    and date (1.event_time) = date(p.event_time)
)

this one i dont understand 
explain in fully 

