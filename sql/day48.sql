-- # TCL(Transaction Control Language)
-- # 1. commit - saves the current transaction
-- # 2. rollback - undo the current transaction
-- # 3. savepoint - creates a savepoint within the current transaction

-- # Transacation:
-- #     A transcation is  nothing but it treats query statements as single unit of of work

-- # ACID Properties:
-- # 1. atomicity - all operations within a transaction are treated as a single unit of work
-- # 2. consistency - the database is consistent within a transaction
-- # 3. isolation - transactions are isolated from each other
-- # 4. durability - the changes made by a transaction are permanent even after the transaction is completed
use bank;
show tables;
select *from accounts;

-- delete entire table data 
truncate table accounts;
delete from accounts;
set sql_safe_updates = 0;

alter table accounts drop column password;
alter table accounts add column AMOUNT int unsigned not null ;
desc accounts;

-- data insertion
insert  into accounts(account_no,amount)
values(101,2000),(102,5000),(103,1000);
select * from accounts; 

-- rollback
-- Transfer 2000 from 101 to 103
start transaction;
-- debit 2000 from 101 account
update accounts set amount = amount -  2000 where account_no = 101;
-- credit 2000 into 103
update accounts set amount = amount +  2000 where account_no = 103;
rollback;
select *  from accounts;

-- commit
-- debit 1000 from 102 account
update accounts set amount = amount -  1000 where account_no = 102;
-- credit 2000 into 103
update accounts set amount = amount +  1000 where account_no = 103;
commit;
select *  from accounts;

-- savepoint
-- debit 1000 from 102 account and credit to 101
update accounts set amount = amount -  1000 where account_no = 102;
update accounts set amount = amount +  1000 where account_no = 101;
SAVEPOINT s1;
-- debit 1000 from 102 account and credit to 103
update accounts set amount = amount -  1000 where account_no = 102;
update accounts set amount = amount +  1000 where account_no = 103;
savepoint s3;

select *  from accounts;
rollback to s1;
select *  from accounts;
