-- Sub-query:
-- A query contains one more query that query we can call it as sub query or inner query
-- types:
-- 1.single row sub-query
-- 2. multi row sub-query
-- eg:
-- main query(sub-query)
-- in execution process the sub-query executes first,later main query executes
--   
use it_company1;
select *from employee;
-- return ram's department employee detail
select deptid from employee
where name="RAM";
-- using sub queries
select*from employee
where deptid=(select deptid from employee
where name="RAM");
-- return employee those whose salaries are morethan average salaries of employees using sub queries
select * from employee 
where salary >
(select avg(salary) from employee);
-- return the rams dept employee details without rams details
SELECT *FROM employee
WHERE deptid = (
    SELECT deptid FROM employee WHERE name = 'RAM')and name !="RAM";
-- return employee details whose salary is greater than the 1001 depts min salary
select * from employee
where salary > any(select salary from employee where deptid = 1001);
-- return employee details whose salary  is less than akk 1002's dept employee salary
select * from employee
where salary < All(select salary from employee where deptid = 1002);
-- reutrn employee names whose name dosent belong to 1003 dept
select * from employee
where name not in (select name from employee where deptid= 1003);  
