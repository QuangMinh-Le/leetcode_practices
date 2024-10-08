SELECT DISTINCT firstName, lastName, city, state
FROM Person 
JOIN Address 
ON Person.personId = Address.personId