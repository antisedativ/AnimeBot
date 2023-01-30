import pymysql

from config import HOST, USER, PASSWORD, DB_NAME


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
        print("Connecting...")
        print('#' * 20)

    except Exception as ex:
        print("#" * 20)
        print('Error...')
        print(ex)
        print("#" * 20)


async def db_add_user(user_id, username, firstname, lastname, chat_id):

    print("INSERT INTO `users`(user_id, username, firstname, lastname, chat_id) " \
          f"VALUES ('{user_id}', '{username}', '{firstname}', '{lastname}', '{chat_id}');")

    # insert data
    # with connection.cursor() as cursor:
    #     insert_query = "INSERT INTO `users`(user_id, username, firstname, lastname, chat_id) " \
    #                    "VALUES ('{user_id}', '{username}', '{firstname}', '{lastname}', '{chat_id}');"
    #     cursor.execute(insert_query)
    #     connection.commit()


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

