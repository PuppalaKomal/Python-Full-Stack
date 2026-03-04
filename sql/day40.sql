-- create new datebase database
create database if not exists datasets;
-- select database
use datasets;
-- check table data
select *from tips;
-- describe table
-- change smoker, date and time datatype into varchar
alter table tips modify smoker varchar(20);
alter table tips modify day varchar(20);
alter table tips modify smoker varchar(20);
-- changeing sex to gender
-- alter table table_name rename old_column_name to new_column_name;
alter table tips rename column sex to gender;
alter table tips modify gender enum("Male","Female");
-- selecting smoker data
select distinct smoker from tips;
-- changing data type for smoker 
alter table tips modify smoker enum("YES","NO") not null;
alter table tips modify size int not null default 1 ;
-- select record whose size is 3
SELECT * FROM tips
WHERE size = 3;
-- FIND MALE SMOKER RECORDS
select * from tips
where gender = "Male"
and smoker = "YES";
-- FIND FEMALE NON SMOKERS RECORDS
select * from tips
where gender = "Female"
and smoker = "NO"; 
-- FIND FRIDAY TOTAL BILL
select sum(total_bill) as "friday total bill " from tips where day = "fri" ;
select ROUND(sum(total_bill),1) as "friday total bill " from tips where day = "fri" ;
-- select TOTAL BILL AFTER GIVING 10% DISCOUNT ON THE TOTAL BILL
SELECT total_bill,total_bill - (total_bill * 0.10) AS discounted_bill
FROM tips;
-- find male customers minimum and maximum bill
SELECT MIN(total_bill) AS min_bill,MAX(total_bill) AS max_bill
FROM tips
WHERE gender = 'Male';
-- return smoker and non smoker count
SELECT smoker, COUNT(*) AS count FROM tips
GROUP BY smoker;
-- return female smoker and non smoker count
SELECT GENDER,smoker, COUNT(*) AS count FROM tips
WHERE GENDER ="Female" GROUP BY smoker;
-- find total bill of dinner time as per the gender
SELECT gender, SUM(total_bill) AS total_dinner_bill
FROM tips
WHERE time = 'Dinner'
GROUP BY gender;
-- return top 5 total bills
select * from tips order by total_bill desc
limit 5; 
-- return all records as per total bill in descending order
SELECT * 
FROM tips
ORDER BY total_bill DESC;

