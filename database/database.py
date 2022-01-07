import mysql.connector

from credentials import credentials_database as credentials


connection =  mysql.connector.connect(
    host=credentials.host,
    user=credentials.user,
    passwd=credentials.password,
    port=credentials.port,
    database=credentials.database
)
