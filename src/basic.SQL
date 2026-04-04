select date(event_time) as event_date,
        count(distinct user_id) as dau
from events
group by event_date
order by event_date;

