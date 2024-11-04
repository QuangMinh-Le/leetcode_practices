SELECT product_name, year, price
From Sales Left Join Product 
On Sales.product_id = Product.product_id