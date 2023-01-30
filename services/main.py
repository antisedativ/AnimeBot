import pymysql

from config import HOST, USER, PASSWORD, DB_NAME

try:
    connection = pymysql.connect(
        host=HOST,
        port=3306,
        user=USER,
        password=PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connecting...")
    print('#' * 20)

    try:
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM users;"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            print("#" * 20)

    finally:
        connection.close()


except Exception as ex:
    print('Error...')
    print(ex)