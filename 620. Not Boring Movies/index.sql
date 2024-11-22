SELECT id, movie, description, rating
FROM Cinema
Where id % 2 = 1
And description != 'boring'
ORDER BY rating desc 