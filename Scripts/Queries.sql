-- ==============================================================================
-- PROJECT: Title Operations SLA Audit
-- AUTHOR: Alpha Oumar II Bah
-- PURPOSE: Diagnostic queries to identify SLA breaches and interest penalty risk
-- ==============================================================================
-- 1. LENDER EFFICIENCY
-- Show the average processing time for each lender and the 14-day gap between Fairstone and the other lenders.
SELECT 
    Lender,
    ROUND(AVG(DATEDIFF(Date_Funded, Date_Received)),0) AS Avg_Processing_Days
FROM fct_data
GROUP BY Lender
ORDER BY Avg_Processing_Days DESC;


--2. 
