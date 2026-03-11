-- STRING FUNCTIONS
-- NOTE: IN SQL INDEXING STARTS FROM 1
-- case conversion --UPPERCASE() OR UCASE; LOWERCASE() OR LCASE
SELECT UPPER('hello world') AS upper_text;
SELECT LOWER('HELLO WORLD') AS lower_text;
-- string padding -- LPAD(STR,LENGTH,PAD_STR);RPAD(STR,LENGTH,PAD_STR)
SELECT LPAD('SQL', 8, '*') AS left_padded;
SELECT RPAD('SQL', 8, '*') AS right_padded;
-- white space removal --TRIM(STR);LTRIM(STR);RTRIM(STR)
SELECT TRIM('   SQL Query   ') AS trimmed_text;
SELECT LTRIM('   SQL Query') AS left_trimmed;
SELECT RTRIM('SQL Query   ') AS right_trimmed;
-- string concatination --CONCAT(STR1,STR2);CONCAT_WS(STR1,STR2)
SELECT CONCAT('Hello', ' ', 'World') AS full_text;
SELECT CONCAT_WS('-', '2026', '03', '11') AS date_format;
-- sub string EXTRACTION  --LEFT(STR,LENGTH);RIGHT(STR,LENGTH);SUBSTRING(STR,LENGTH)
SELECT LEFT('DATABASE', 4) AS left_text;

-- DATETIME FUNCTION (YYYY-MM-DD)(HH:MM:SS)
-- date(datetime) --YEAR(DATE);MONTH(DATE);DAY(DATE)
-- time(datetime) --HOUR(TIME);MINUTE(TIME);SECONDS(TIME)
-- curdate() or current_date()
-- curtime() or current_time()
-- now() or current_timestamp()
-- date_format(date,format)
select DATE_FORMAT("2024-12-25","%d/%m/%y");

-- Numeric functions:
-- ABS(val)
SELECT ABS(-10) AS absolute_value;
-- sqrt(val)
SELECT SQRT(64) AS square_root;
-- pow(val,power)
SELECT POW(2,3) AS power_value;
-- log(val)
SELECT LOG(10) AS log_value;
-- decimal value rounding:
-- round(val,position)
SELECT ROUND(25.6789,2) AS rounded_value;
-- floor(val)
SELECT FLOOR(15.89) AS floor_value;
-- ceil(val)
SELECT CEIL(15.21) AS ceil_value;
-- truncate(val,dot)
SELECT TRUNCATE(25.6789,2) AS truncated_value;
