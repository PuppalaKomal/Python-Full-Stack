# import mysql connector 
import mysql.connector as SQLC
# database config
database_config=SQLC.connect(
    host = 'localhost',
    user = 'root',
    password='root',
    database = 'bank' # mysql password 
)
# cursor object creation 
cursor = database_config.cursor(dictionary=True)
# creating database
# cursor.execute("CREATE DATABASE if not exists bank;")
# print("database is created")
# print(database_config)
# print(cursor)

# query = """
# CREATE TABLE IF NOT EXISTS ACCOUNTS (
#     ACCOUNT_NO INT PRIMARY KEY,
#     PASSWORD VARCHAR(50)
# );
# """
# cursor.execute(query)
# print("Table Created")

# #adding data in table
# insert_data_into_table="""
# INSERT INTO ACCOUNTS (ACCOUNT_NO, PASSWORD) VALUES (%s, %s);
# """
# # #execute query
# cursor.execute(insert_data_into_table, (1234, 1234))
# print("Data Inserted")
# #inseting many records
# values = [(12345, 12345), (5678, 5678), (9101, 9101)]
# cursor.executemany(insert_data_into_table, values)
# print("Data Inserted")
# #commiting in database
# database_config.commit()

# cursor.execute("SELECT * FROM ACCOUNTS")
# print(cursor)

# #fetch function
# print(cursor.fetchone())
# print(cursor.fetchall())

#get 12345 password
cursor.execute("SELECT PASSWORD FROM ACCOUNTS WHERE ACCOUNT NO = %s ", (12345,))
print(cursor.fetchone(),[0])
