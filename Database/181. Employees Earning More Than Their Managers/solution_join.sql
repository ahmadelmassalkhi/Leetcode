# Write your MySQL query statement below

SELECT E.name AS 'Employee'
FROM Employee AS E
JOIN Employee AS M
ON M.id = E.managerId
WHERE M.salary < E.salary