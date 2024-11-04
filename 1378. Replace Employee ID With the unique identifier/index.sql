Select unique_id, name
From Employees
Left Join EmployeeUNI
ON Employees.id = EmployeeUNI.id
