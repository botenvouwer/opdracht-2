-- Zodra we een coherent domeinmodel hebben kunnen we modelleren met onze data
-- Op basis van het domeinmodel kunnen we bijvoorbeeld een view, materialised view of een nieuwe entiteit voor onze visualisatie maken
-- Je kunt een table vullen vanuit een query -> zie https://learnsql.com/cookbook/how-to-create-one-table-from-another-table-in-sql/

-- Wat zijn de top 3 producten die wij per maand verkopen;
-- Welke medewerker verkoopt per jaar de meeste producten;
-- Een top 10 van welke klanten de meeste bestellingen gedaan hebben;
-- Een top 10 van welke klanten overall de meeste producten gekocht hebben;
-- Een top 10 van welke klanten overall de hoogste opbrengsten gegenereerd hebben.

-- views en tabellen net voordat ze in Matplotlib gaan

DO $$ DECLARE
    r RECORD;
BEGIN
    -- Drop all views in the 'models' schema
    FOR r IN (SELECT viewname FROM pg_views WHERE schemaname = 'models') LOOP
        EXECUTE 'DROP VIEW IF EXISTS models.' || quote_ident(r.viewname) || ' CASCADE';
    END LOOP;
END $$;


-- Top 3 products based on order_qty in month 7
DROP VIEW IF EXISTS models.top_selling_products;
CREATE VIEW models.top_selling_products AS
SELECT p.product_name, SUM(d.order_qty) AS total_order_qty
FROM domain.order_details d
JOIN domain.products p ON d.product_id = p.product_id
JOIN domain.orders o ON o.sales_order_id = d.sales_order_id
WHERE EXTRACT(MONTH FROM o.order_date) = 7
GROUP BY p.product_id,p.product_name
ORDER BY total_order_qty DESC
LIMIT 3;


-- Top customers based on revenue unit_price
DROP VIEW IF EXISTS models.top_costumers_revenue;
CREATE VIEW models.top_customers_revenue AS
SELECT c.full_name, ROUND(SUM(d.order_qty * d.unit_price)::NUMERIC, 2) AS total_amount_spent
FROM domain.order_details d
JOIN domain.products p ON d.product_id = p.product_id
JOIN domain.orders o ON o.sales_order_id = d.sales_order_id
JOIN domain.customers c ON o.customer_id = c.customer_id
GROUP BY c.full_name
ORDER BY total_amount_spent DESC
LIMIT 10;

-- Top customers based on profit = list_price - standard_cost
DROP VIEW IF EXISTS models.top_costumers_profit;
CREATE VIEW models.top_customers_profit AS
SELECT c.full_name, ROUND(SUM(d.order_qty * (p.list_price - p.standard_cost))::NUMERIC, 2) AS total_amount_spent
FROM domain.order_details d
JOIN domain.products p ON d.product_id = p.product_id
JOIN domain.orders o ON o.sales_order_id = d.sales_order_id
JOIN domain.customers c ON o.customer_id = c.customer_id
GROUP BY c.full_name
ORDER BY total_amount_spent DESC
LIMIT 10;

-- Top customers based on order qty
DROP VIEW IF EXISTS models.top_costumers_order_qty;
CREATE VIEW models.top_costumers_order_qty AS
SELECT c.full_name, SUM(d.order_qty) AS total_order_qty
FROM domain.order_details d
JOIN domain.products p ON d.product_id = p.product_id
JOIN domain.orders o ON o.sales_order_id = d.sales_order_id
JOIN domain.customers c ON o.customer_id = c.customer_id
GROUP BY c.full_name
ORDER BY total_order_qty DESC
LIMIT 10;

-- Top employees based on order_qty
DROP VIEW IF EXISTS models.top_employees_order_qty;
CREATE VIEW models.top_employees_order_qty AS
SELECT e.full_name, SUM(d.order_qty) AS total_order_qty
FROM domain.order_details d
JOIN domain.orders o ON o.sales_order_id = d.sales_order_id
JOIN domain.employees e ON o.employee_id = e.employee_id
GROUP BY e.full_name
ORDER BY total_order_qty DESC
LIMIT 10;


-- Top employees based on profit
DROP VIEW IF EXISTS models.top_employees_profit;
CREATE VIEW models.top_employees_profit AS
SELECT e.full_name, ROUND(SUM(d.order_qty * (p.list_price - p.standard_cost))::NUMERIC, 2) AS total_profit
FROM domain.order_details d
JOIN domain.orders o ON o.sales_order_id = d.sales_order_id
JOIN domain.employees e ON o.employee_id = e.employee_id
JOIN domain.products p ON p.product_id = d.product_id
GROUP BY e.full_name
ORDER BY total_profit DESC
LIMIT 10;

-- Top 5 products from top customer (Why does Joseph need 426 pairs of socks?!)
DROP VIEW IF EXISTS models.top_products_customer_615;
CREATE VIEW models.top_products_customer_615 AS
SELECT p.product_name, SUM(d.order_qty) AS total_order_qty
FROM domain.order_details d
JOIN domain.products p ON p.product_id = d.product_id
GROUP BY p.product_name
ORDER BY total_order_qty DESC
LIMIT 5;
