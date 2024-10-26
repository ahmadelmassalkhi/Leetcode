# Write your MySQL query statement below

SELECT E.name AS 'Employee'
FROM Employee AS E
WHERE E.salary > (
    SELECT M.salary
    FROM Employee AS M -- Manager
    WHERE M.id = E.managerId
)