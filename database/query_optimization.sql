-- From :
select
  *
from
  costumer o
  inner join dt_sales ds on o.cust_id = ds.cust_id
  inner join dt_product dp on ds.product_id = dp.product_id;

-- Optimization :
-- Usahakan Tidak Men Select semua (*) field yang ada dalam table saat join maupun tidak , karena itu berpengaruh kepada perfoma query saat mengambil data .
-- kurangi mengambil field yang memiliki size yang besar seperti contohnya field dengan data geometry
select
  o.cust_id , o.cust_address , dp.product_name , dp.product_price , ds.product_quantity
from
  costumer o
  inner join dt_sales ds on o.cust_id = ds.cust_id
  inner join dt_product dp on ds.product_id = dp.product_id;

-- From :
select
  o.cust_id , o.cust_address , dp.product_name , ds.product_quantity
from
  costumer o
  inner join dt_sales ds on o.cust_id = ds.cust_id
  inner join dt_product dp on ds.product_id = dp.product_id
where o.cust_id=102255;

-- Optimization :
-- Usahakan Menggunakan CTE (Common Table Expressions) , hindari melakukan filter setelan melakukan join.
-- hal tersebut akan mempengaruhin performa saat select data karena , sql akan melakukan join terhadap semua field terlebih dahulu dan setelah itu hasil join tersebut di filter lagi jadi sql akan memproses data secara 2 kali
-- Jika Menggunakan CTE Maka Data akan di filter terlebihdahulu setelah itu di join
with data as (
    select
      o.cust_id , o.cust_address
    from
      costumer o
    where cust_id=102255
) select o.* , dp.product_name , ds.product_quantity from data o
  inner join dt_sales ds on o.cust_id = ds.cust_id
  inner join dt_product dp on ds.product_id = dp.product_id;

-- Cara Ini juga bisa di lakukan saat kita melakukan operasi aggregasi terhadap table :
with data as (
    select
       dp.product_id,
       dp.product_name,
       sum(case when o.cust_age <= 26 then dp.product_price end) as gen_z_sales,
       sum(case when o.cust_age >= 27 and o.cust_age <= 42  then dp.product_price end) as milenial_sales,
       sum(case when o.cust_age >= 43 and o.cust_age <= 58 then dp.product_price end) as gen_x_sales,
       sum(case when o.cust_age >= 59 and o.cust_age <= 77 then dp.product_price end) as baby_boomer_sales
       from costumer o inner join dt_sales ds on o.cust_id = ds.cust_id
  inner join dt_product dp on ds.product_id = dp.product_id
  where dp.product_id=168
  group by dp.product_id, dp.product_name
) select * from data;