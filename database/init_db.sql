CREATE TABLE costumer (
  cust_id SERIAL,
  cust_address text,
  cust_age integer,
  effective_start_date DATE,
  effective_end_date DATE,
  current_ind VARCHAR(10)
);

COPY costumer(cust_id, cust_address, cust_age, effective_start_date,effective_end_date,current_ind)
FROM 'D:\learn python\python\project_ebdesk\flaskr\dts_customer_dim.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE dt_product (
  product_id SERIAL,
  product_name varchar(225),
  product_price float,
  effective_start_date DATE,
  effective_end_date DATE,
  current_ind VARCHAR(10)
)

COPY dt_product(product_id, product_name, product_price, effective_start_date,effective_end_date,current_ind)
FROM 'D:\learn python\python\project_ebdesk\flaskr\dts_product_dim.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE dt_sales (
  order_id SERIAL,
  product_id SERIAL,
  cust_id SERIAL,
  product_quantity INTEGER,
  order_date DATE
);

COPY dt_sales(order_id, product_id , cust_id, product_quantity,order_date)
FROM 'D:\learn python\python\project_ebdesk\flaskr\dts_sales_transactions.csv'
DELIMITER ','
CSV HEADER;