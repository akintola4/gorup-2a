import mysql.connector

# Function to create the 'excos' database and 'excos' table
def create_database_and_table():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="tester",
            password="test"
        )
        cursor = conn.cursor()

        # Create the 'excos' database
        cursor.execute("CREATE DATABASE IF NOT EXISTS excos")

        # Switch to the 'excos' database
        cursor.execute("USE excos")

        # Create the 'excos' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS excos (
                matric_no INT PRIMARY KEY,
                name VARCHAR(255),
                department VARCHAR(255),
                office VARCHAR(255)
            )
        ''')

        print("Database and table created successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        cursor.close()
        conn.close()

# Function to insert a new element into the 'excos' table
def insert_element(matric_no, name, department, office):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="tester",
            password="test",
            database="excos"
        )
        cursor = conn.cursor()

        # Insert the new element
        cursor.execute("INSERT INTO excos (matric_no, name, department, office) VALUES (%s, %s, %s, %s)",
                       (matric_no, name, department, office))

        conn.commit()
        print("New element added successfully!")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        cursor.close()
        conn.close()

# Function to display the full 'excos' database
def display_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="tester",
            password="test",
            database="excos"
        )
        cursor = conn.cursor()

        # Retrieve all elements from the 'excos' table
        cursor.execute("SELECT * FROM excos")
        records = cursor.fetchall()

        # Display the full database
        for record in records:
            print("Matric No:", record[0])
            print("Name:", record[1])
            print("Department:", record[2])
            print("Office:", record[3])
            print("-----------------------")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        cursor.close()
        conn.close()

# Main program
if __name__ == "__main__":
    # Create the 'excos' database and 'excos' table if they don't exist
    create_database_and_table()

    while True:
        print("\nOptions:")
        print("1. Add New Element")
        print("2. Display Full Database")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            matric_no = int(input("Enter Matric No: "))
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            office = input("Enter Office: ")
            insert_element(matric_no, name, department, office)
        elif choice == '2':
            display_database()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select again.")
