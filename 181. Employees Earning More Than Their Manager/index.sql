Select 
e1.name as Employee
From Employee e1 
Inner Join Employee e2
On e2.id = e1.managerId
Where e1.salary > e2.salary