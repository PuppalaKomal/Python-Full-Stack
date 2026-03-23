import mysql.connector as SQLC
def DatabaseConfig():
    connection = SQLC.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "bank"
    )
    return connection
