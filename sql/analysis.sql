-- Average salary per department
SELECT department, AVG(salary)
FROM employees
GROUP BY department;

-- Highest sales employee
SELECT name, monthly_sales
FROM employees
ORDER BY monthly_sales DESC
LIMIT 1;

-- Employees with 5+ years experience
SELECT name, department
FROM employees
WHERE experience >= 5;
