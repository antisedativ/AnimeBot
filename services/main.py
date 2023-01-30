import pymysql

#127.0.0.1
host = 'localhost'
user = 'root'
password = '10200226Artem'
db_name = 'senpai_bot'

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
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