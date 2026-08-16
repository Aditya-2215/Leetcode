SELECT today.id
FROM weather today
JOIN weather yesterday
ON today.recordDate - 1 = yesterday.recordDate
WHERE today.temperature > yesterday.temperature;