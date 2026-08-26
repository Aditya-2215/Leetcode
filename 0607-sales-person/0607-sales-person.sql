SELECT sp.name
FROM SalesPerson sp
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    JOIN Company c
        ON o.com_id = c.com_id
    WHERE o.sales_id = sp.sales_id
      AND c.name = 'RED'
);