SELECT sector, ticker, price
FROM (
    SELECT 
        c.sector,
        c.ticker,
        m.price,
        ROW_NUMBER() OVER (
            PARTITION BY c.sector 
            ORDER BY m.price DESC
        ) AS rn
    FROM company_info c
    JOIN market_data m 
    ON c.ticker = m.ticker
) t
WHERE rn = 1;