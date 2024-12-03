
SELECT  
   Prices.product_id
   ,coalesce( ROUND(SUM(Prices.price * UnitsSold.units) / Sum(UnitsSold.units), 2) , 0) As average_price
FROM Prices
Left JOIN UnitsSold
ON (UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date)
and Prices.product_id = UnitsSold.product_id
Group by Prices.product_id