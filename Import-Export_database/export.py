import csv
import os
import psycopg2
from config import host, user, password, db_name

# File path and name.
filePath = 'c:\\Temp\\'
fileName = 'partexport.csv'

# Check if the file path exists.
if os.path.exists(filePath):

    try:

        connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
        )
        connection.autocommit = True

    except psycopg2.DatabaseError as e:

        # Confirm unsuccessful connection and stop program execution.
        print("Database connection unsuccessful.")
        quit()

    # Cursor to execute query.
    cursor = connection.cursor()

    # SQL to select data from the person table.
    sqlSelect = \
        "SELECT id, machine_id, person_name, transaction_date, status \
         FROM machine_transactions \
         ORDER BY id"

    try:

        # Execute query.
        cursor.execute(sqlSelect)

        # Fetch the data returned.
        results = cursor.fetchall()

        # Extract the table headers.
        headers = [i[0] for i in cursor.description]

        # Open CSV file for writing.
        csvFile = csv.writer(open(filePath + fileName, 'w', newline=''),
                             delimiter=',', lineterminator='\r\n',
                             quoting=csv.QUOTE_ALL, escapechar='\\')

        # Add the headers and data to the CSV file.
        csvFile.writerow(headers)
        csvFile.writerows(results)

        # Message stating export successful.
        print("Data export successful.")

    except psycopg2.DatabaseError as e:

        # Message stating export unsuccessful.
        print("Data export unsuccessful.")
        quit()

    finally:

        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

else:

    # Message stating file path does not exist.
    print("File path does not exist.")