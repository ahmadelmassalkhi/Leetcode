SELECT W.id
FROM Weather AS W
WHERE W.temperature > (
    SELECT T.temperature
    FROM Weather AS T
    WHERE DATEADD(DAY, -1, W.recordDate) = T.recordDate
);
