from flask import Flask, render_template, request
import psycopg2
from config import host, user, password, db_name

app = Flask(__name__)

# Configure database connection
connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
# Create a cursor object
cursor = connection.cursor()
connection.autocommit = True

# Define route to display machine movements
@app.route('/')
@app.route('/machine_movements')
def machine_movements():
    # Retrieve machine ID from request parameter
    machine_id = request.args.get('machine_id')
    
    # Query database for machine movements
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM machine_transactions WHERE machine_id = %s", (machine_id,))
        movements = cursor.fetchall()

        # Query database for total number of unique machine IDs
        cursor.execute("SELECT id FROM machine_transactions")
        id = cursor.fetchone()[0]

        cursor.execute("SELECT machine_id FROM machine_transactions")
        machine_id = cursor.fetchone()[0]

        cursor.execute("SELECT person_name FROM machine_transactions")
        person_name = cursor.fetchone()[0]

        cursor.execute("SELECT transaction_date FROM machine_transactions")
        transaction_date = cursor.fetchone()[0]

        cursor.execute("SELECT status FROM machine_transactions")
        status = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(DISTINCT machine_id) FROM machine_transactions")
        total_machine_count = cursor.fetchone()[0]
        
    # Render template with machine movements and total machine count
    return render_template("machine_movements.html", machine_id=machine_id, movements=movements, total_machine_count=total_machine_count, id=id, person_name=person_name, transaction_date=transaction_date, status=status)

if __name__ == '__main__':
    app.run()

