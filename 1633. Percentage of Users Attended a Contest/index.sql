SELECT contest_id, Round(Count(distinct user_id)/(Select count(user_id) from Users) * 100, 2) as percentage
FROM Register
Group By contest_id
ORDER BY percentage desc, contest_id