Select Employee.name, Bonus.bonus
From Employee
Left Join Bonus
on Bonus.empId = Employee.empId
Where Bonus.bonus < 1000
Or Bonus.bonus is NULL