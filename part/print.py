import psycopg2
from config import host, user, password, db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT Version();"
        )

        print(f"Server version: {cursor.fetchone()}") 

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         CREATE TABLE vendor_parts (
    #         vendor_id INTEGER NOT NULL            
    #         )
    #         """)

    
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT id, name, quantity, location FROM parts ORDER BY id;"""
    #     )

    #     print(f"Server version: {cursor.fetchone()}")
    #     print(f"Server version: {cursor.fetchone()}")
    #     print(f"Server version: {cursor.fetchone()}")


except Exception as _ex:
    print("[INFO] Error db:", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")