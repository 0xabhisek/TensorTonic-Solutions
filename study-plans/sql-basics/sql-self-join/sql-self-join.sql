-- Write your SQL query here
select u1.username, coalesce(u2.username, 'organic') as referrer_name
from user_referrals u1 left join user_referrals u2 
on u1.referred_by = u2.id
order by u1.username;
