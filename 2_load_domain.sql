-- Zodra je een raw laag hebt in de database kunnen we dmv queries ons domeinmodel opbouwen
-- Schrijf de queries die we nodig hebben op een domeinmodel op te bouwen
-- Je kunt een table vullen vanuit een query -> zie https://learnsql.com/cookbook/how-to-create-one-table-from-another-table-in-sql/

-- Tabel customers van raw naar domain
CREATE TABLE IF NOT EXISTS domain.customers(
    customer_id INT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    full_name TEXT
);
INSERT INTO domain.customers
SELECT
    customer_id::INT,
    first_name,
    last_name,
    full_name
FROM raw.customers;

-- ORDERS: Opgesplitste orders tabel 1: orders
CREATE TABLE IF NOT EXISTS domain.orders(
    sales_order_id INT,
    order_date TIMESTAMP,
    due_date TIMESTAMP,
    ship_date TIMESTAMP,
    employee_id INT,
    customer_id INT,
    sub_total DECIMAL(10, 2),
    tax_amt DECIMAL(10, 2),
    freight DECIMAL(10, 2),
    total_due DECIMAL(10, 2)
);

INSERT INTO domain.orders (sales_order_id, order_date, due_date, ship_date, employee_id, customer_id, sub_total, tax_amt, freight, total_due)
SELECT DISTINCT
    sales_order_id::INT,
    order_date::TIMESTAMP,
    due_date::TIMESTAMP,
    ship_date::TIMESTAMP,
    employee_id::INT,
    customer_id::INT,
    sub_total::DECIMAL(10,2),
    tax_amt::DECIMAL(10,2),
    freight::DECIMAL(10,2),
    total_due::DECIMAL(10,2)
FROM
    raw.orders;

-- ORDERS: Opgesplitste orders tabel 2: order_details
CREATE TABLE IF NOT EXISTS domain.order_details (
    sales_order_detail_id INT,
    sales_order_id INT,
    product_id INT,
    order_qty INT,
    unit_price DECIMAL(10, 2),
    unit_price_discount DECIMAL(10, 2),
    line_total DECIMAL(10, 2)
);

INSERT INTO domain.order_details (sales_order_detail_id, sales_order_id, product_id, order_qty, unit_price, unit_price_discount, line_total)
SELECT
    sales_order_detail_id::INT,
    sales_order_id::INT,
    product_id::INT,
    order_qty::INT,
    unit_price::DECIMAL(10,2),
    unit_price_discount::DECIMAL(10,2),
    line_total::DECIMAL(10,2)
FROM
    raw.orders;

-- Tabel productcategories van raw naar domain

CREATE TABLE IF NOT EXISTS domain.productcategories (
    category_id INT,
    category_name TEXT
);

INSERT INTO domain.productcategories(category_id,category_name)
SELECT
    category_id::INT,
    category_name
FROM
    raw.productcategories;

-- Table products from raw to domain
CREATE TABLE IF NOT EXISTS domain.products (
    product_id INT,
    product_number TEXT,
    product_name TEXT,
    model_name TEXT,
    make_flag BOOLEAN,
    standard_cost DECIMAL(10,2),
    list_price DECIMAL(10,2),
    sub_category_id INT
);

INSERT INTO domain.products(product_id, product_number, product_name, model_name, make_flag, standard_cost, list_price, sub_category_id)
SELECT
    product_id::INT,
    product_number,
    product_name,
    model_name,
    make_flag::BOOLEAN,
    standard_cost::DECIMAL(10,2),
    list_price::DECIMAL(10,2),
    sub_category_id::INT
FROM raw.products;

-- Tabel productsubcategories van raw naar domain

CREATE TABLE IF NOT EXISTS domain.productsubcategories (
    sub_category_id INT,
    category_id INT,
    sub_category_name TEXT
);

INSERT INTO domain.productsubcategories(sub_category_id, category_id, sub_category_name)
SELECT
    sub_category_id::INT,
    category_id::INT,
    sub_category_name
FROM raw.productsubcategories;

-- Tabel vendorproduct van raw naar domain

CREATE TABLE IF NOT EXISTS domain.vendorproduct(
    product_id INT,
    vendor_id INT
);

INSERT INTO domain.vendorproduct(product_id, vendor_id)
SELECT
    product_id::INT,
    vendor_id::INT
FROM raw.vendorproduct;

-- Table vendors from raw to domain

CREATE TABLE IF NOT EXISTS domain.vendors(
    vendor_id INT,
    vendor_name TEXT,
    account_number TEXT,
    credit_rating INT,
    active_flag BOOLEAN
);

INSERT INTO domain.vendors(vendor_id, vendor_name, account_number, credit_rating, active_flag)
SELECT
    vendor_id::INT,
    vendor_name,
    account_number,
    credit_rating::INT,
    active_flag::BOOLEAN
FROM raw.vendors
;

-- Weet niet of het de bedoeling is om dingen aan te passen in raw
-- Maar de string 'NULL' values moeten omgezet naar gewone NULL's
UPDATE raw.employees
SET manager_id = NULL WHERE manager_id = 'NULL';
UPDATE raw.employees
SET territory = NULL WHERE territory = 'NULL';
UPDATE raw.employees
SET country = NULL WHERE country = 'NULL';
UPDATE raw.employees
SET "group" = NULL WHERE "group" = 'NULL';

-- tabel Employees van raw naar domain

CREATE TABLE IF NOT EXISTS domain.employees(
    employee_id INT,
    manager_id INT,
    first_name TEXT,
    last_name TEXT,
    full_name TEXT,
    job_title TEXT,
    organization_level INT,
    marital_status CHAR(1),
    gender CHAR(1),
    territory TEXT,
    country CHAR(2),
    "group" TEXT
)

INSERT INTO domain.employees(employee_id, manager_id, first_name, last_name, full_name, job_title, organization_level, marital_status, gender, territory, country, "group")
SELECT
    employee_id::INT,
    manager_id::INT,
    first_name,
    last_name,
    full_name,
    job_title,
    organization_level::INT,
    marital_status::CHAR(1),
    gender::CHAR(1),
    territory,
    country::CHAR(2),
    "group"
FROM raw.employees

