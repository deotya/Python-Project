import psycopg2
from config import host, user, password, db_name


# Connect to the database
connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
# Create a cursor object
cursor = connection.cursor()
connection.autocommit = True

# Create parts table if it does not exist
cursor.execute("""
    CREATE TABLE parts(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        quantity INTEGER,
        location VARCHAR(255)
    )"""
   )

# Create machine_transactions table if it does not exist
cursor.execute("""
    CREATE TABLE machine_transactions(
        id SERIAL PRIMARY KEY,
        machine_id INTEGER,
        person_name VARCHAR(255),
        transaction_date TIMESTAMP,
        status VARCHAR(255)
    )"""
   )

# Commit the changes to the database
#connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()