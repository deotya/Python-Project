import csv
import os
import psycopg2
from config import host, user, password, db_name

# File path and name.
filePath = 'c:\\Temp\\partexport.csv'

# Check if the file path exists.
if os.path.isfile(filePath):

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
    
    # Assign CSV file to reader object.
    reader = csv.DictReader(open(filePath))

    # Record count.
    recordCount = 0


    # Insert person information into the database.
    for row in reader:

        # SQL to insert person information.
        sqlInsert = \
            "INSERT INTO machine_transactions (machine_id, person_name, transaction_date, status)  \
             VALUES (%s, %s, %s, %s)"

        try:

            # Execute query and commit changes.
            cursor.execute(sqlInsert, (row['machine_id'],
                                       row['person_name'],
                                       row['transaction_date'],
                                       row['status']))

            # Increment the record count.
            recordCount += 1


        except psycopg2.DatabaseError as e:

            # Confirm error adding person information and stop program execution.
            print("Error adding person information.")
            quit()

    # connection.close()
    if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

    # Provide feedback on the number of records added.
    if recordCount == 0:

        print("No new person records added.")

    elif recordCount == 1:

        print(str(recordCount) + " person record added.")

    else:

        print(str(recordCount) + " person records added.")



else:

    # Message stating CSV file could not be located.
    print("Could not locate the CSV file.")