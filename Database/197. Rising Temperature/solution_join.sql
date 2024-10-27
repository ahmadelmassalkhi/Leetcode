SELECT W1.id
FROM Weather AS W1
JOIN Weather AS W2
ON DATEADD(DAY, -1, W1.recordDate) = W2.recordDate
WHERE W1.temperature > W2.temperature