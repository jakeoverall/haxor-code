import mysql.connector

# connection_string = "Server=localhost;Port=3306;Database=sakila;Uid=root;Pwd=localhost;"

connection = mysql.connector.connect(
    host="localhost",
    user="codeworks_admin",
    password="password",
    database="codeworks"
)

def get_data(table):
  print(f'--------{table}---------')
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM {table}")
  data = cursor.fetchall()
  for record in data:
      print(record)
  print('\n')


get_data('users')
get_data('courses')
