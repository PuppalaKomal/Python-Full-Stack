use it_company;
-- FIND EMPLOYEE COUNT
select count(id) from employe;
-- FIND SALES EMPLOYEE COUNT
select deptid,count(*) as Count from employe
where deptid = 1003;
-- FIND HR DEPT EMPLOYEE COUNT
select deptid,count(*) as Count from employe
where deptid = 1002;

-- make group dept wise
select name ,deptid,count(*) as Count from employe
group by deptid;
select * from employe ;

-- make total amount to be paid as salaries grp wise
select deptid,count(*) as Count ,sum(salary) from employe
group by deptid;
select * from employe ;

-- find 1001 and 1002 depts employee count
select deptid, count(*) as Count ,sum(salary)from employe
where deptid in (1001, 1002)
group by deptid;

-- select *from employe
select count(id) from employe;
select*from employe;

-- find max salary in each dept
use it_company;
SELECT deptid, MAX(salary) AS max_salary FROM employe
GROUP BY deptid;
-- find min salary in each dept
SELECT deptid, MIN(salary) AS min_salary FROM employe
GROUP BY deptid;
-- find how much average salary company spend
SELECT AVG(salary) AS avg_salary
FROM employe;
-- return 1001 and 1002 depts min salary
select deptid, min(salary) as min_salary from employe
where deptid in (1001, 1002)
group by deptid;
-- return all depts total employees
SELECT deptid, COUNT(*) AS total_employees
FROM employe
GROUP BY deptid;
-- find each dept total salary 
select deptid, sum(salary) as total_salary
from employe
group by deptid;
