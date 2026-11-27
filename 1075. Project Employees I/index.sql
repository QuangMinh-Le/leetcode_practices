SELECT Project.project_id, ROUND(SUM(Employee.experience_years)/COUNT(Project.employee_id), 2) as average_years
FROM Project
Left Join Employee
On Project.employee_id = Employee.employee_id
GROUP BY Project.project_id