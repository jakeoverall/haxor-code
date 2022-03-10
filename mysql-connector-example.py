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


def get_single_item(table, id):
    print(f'--------{table}---------')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table} WHERE id = {id}")
    data = cursor.fetchall()
    print(data)
    print('\n')


def get_user_account(username, password):
    print(f'--------GETTING USER ACCOUNT---------')
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM users WHERE password = {password} AND email = '{username}';")
    data = cursor.fetchall()
    print(data)
    print('\n')


get_user_account('jake@boisecodeworks.com', "'x' OR 1=1")
# get_user_account('t@test.com', 'test')


# get_data('users')
# get_data('courses')


# get_single_item('courses', '2 OR 1=1')
