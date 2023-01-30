import pymysql

from services.config import HOST, USER, PASSWORD, DB_NAME


async def db_connect():
    try:
        global connection
        connection = pymysql.connect(
            host=HOST,
            port=3306,
            user=USER,
            password=PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("#" * 20)
        print("Connected to the database!")
        print('#' * 20)

    except Exception as ex:
        print("#" * 20)
        print('Error...')
        print(ex)
        print("#" * 20)


async def db_add_user(chat_id, username, firstname, lastname, date):
    with connection.cursor() as cursor:
        select_users = f"SELECT 1 FROM users WHERE chat_id = '{chat_id}';"
        cursor.execute(select_users)
        user = cursor.fetchall()

        if not user:
            insert_query = "INSERT INTO `users`(chat_id, username, firstname, lastname, last_message_date) " \
                           f"VALUES ('{chat_id}', '{username}', '{firstname}', '{lastname}', '{date}');"
            cursor.execute(insert_query)
            connection.commit()
        else:
            insert_query = f"UPDATE users SET last_message_date = '{date}' WHERE chat_id = {chat_id};"
            cursor.execute(insert_query)
            connection.commit()


async def db_show_count_users():
    with connection.cursor() as cursor:
        select_all_rows = "SELECT count(chat_id) as count FROM users;"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()
        return rows[0]['count']


async def db_show_users():
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM users;"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()
        print("#" * 20)
        for row in rows:
            print(row)

        print("#" * 20)


async def db_close():
    connection.close()

