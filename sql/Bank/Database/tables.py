from database.connection import DatabaseConfig
def CreateTables():
    db_config=DatabaseConfig()
    cursor=db_config.cursor() 
    users_table_query = """CREATE TABLE IF NOT EXISTS USERS (
                        ACCOUNT INT AUTO_INCREMENT PRIMARY KEY,
                        USERNAME VARCHAR(40) NOT NULL,
                        EMAIL VARCHAR(50) NOT NULL UNIQUE,
                        PHONE VARCHAR(13),
                        ROLE ENUM("USER","ADMIN") DEFAULT "USER" ,
                        )"""
    account_table_query = """CREATE TABLE IF NOT EXISTS ACCOUNTS (
                        ACCOUNT INT,
                        PASSWORD VARCHAR(30) NOT NULL,
                        BALANCE FLOAT UNSIGNED DEFAULT 0.0,
                        FOREIGN KEY(ACCOUNT) REFERENCES USERS(ACCOUNT)
                        )"""
    transactions_table_query = """CREATE TABLE IF NOT EXISTS TRANSACTIONS (
                        TRANSACTIONID INT AUTO_INCREMENT PRIMARY KEY,
                        ACCOUNT INT,
                        AMOUNT FLOAT ,
                        TRANSACTIONTYPE ENUM("DEBIT","CREDIT") NOT NULL,
                        TRANSACTIONTIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY(ACCOUNT) REFERENCES USERS(ACCOUNT)
                        )"""
    cursor.execute(account_table_query)
    cursor.execute(users_table_query)
    cursor.execute(transactions_table_query)
    db_config.commit()
    cursor.close()
    db_config.close()
    
