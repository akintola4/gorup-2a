import mysql.connector

# Function to create the 'excos' and 'ex_excos' databases and tables
def create_databases_and_tables():
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

        # Create the 'ex_excos' database
        cursor.execute("CREATE DATABASE IF NOT EXISTS ex_excos")

        # Switch to the 'ex_excos' database
        cursor.execute("USE ex_excos")

        # Create the 'ex_excos' table (similar structure to 'excos')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ex_excos (
                matric_no INT PRIMARY KEY,
                name VARCHAR(255),
                department VARCHAR(255),
                office VARCHAR(255)
            )
        ''')

        print("Databases and tables created successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        cursor.close()
        conn.close()

# Function to register a new EXCO
def register_exco(matric_no, name, department, office, from_ex_excos=False):
    try:
        conn = mysql.connector.connect(
                        host="localhost",
            user="tester",
            password="test",
            database="excos" if not from_ex_excos else "ex_excos"
        )
        cursor = conn.cursor()

        # Remove the past EXCO with the same office if exists
        cursor.execute("DELETE FROM excos WHERE office = %s", (office,))
        cursor.execute("DELETE FROM ex_excos WHERE office = %s", (office,))

        # Transfer the past EXCO record to EX_OFFICIAL
        cursor.execute("INSERT INTO ex_officials (matric_no, name, department, office) SELECT matric_no, name, department, office FROM excos WHERE office = %s", (office,))
        cursor.execute("INSERT INTO ex_officials (matric_no, name, department, office) SELECT matric_no, name, department, office FROM ex_excos WHERE office = %s", (office,))

        # Register the new EXCO
        cursor.execute("INSERT INTO excos (matric_no, name, department, office) VALUES (%s, %s, %s, %s)",
                       (matric_no, name, department, office))

        conn.commit()
        print("New EXCO registered successfully!")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        cursor.close()
        conn.close()

# Function to display both databases
def display_databases():
    try:
        conn = mysql.connector.connect(
                        host="localhost",
            user="tester",
            password="test"
        )
        cursor = conn.cursor()

        # Show the 'excos' database
        cursor.execute("SHOW DATABASES LIKE 'excos'")
        excos_db_exists = cursor.fetchone()

        if excos_db_exists:
            cursor.execute("USE excos")
            cursor.execute("SELECT * FROM excos")
            excos_records = cursor.fetchall()
            print("\nEXCOS Database:")
            for record in excos_records:
                print(record)

        # Show the 'ex_excos' database
        cursor.execute("SHOW DATABASES LIKE 'ex_excos'")
        ex_excos_db_exists = cursor.fetchone()

        if ex_excos_db_exists:
            cursor.execute("USE ex_excos")
            cursor.execute("SELECT * FROM ex_excos")
            ex_excos_records = cursor.fetchall()
            print("\nEX-EXCOS Database:")
            for record in ex_excos_records:
                print(record)

        # Show the 'ex_officials' database
        cursor.execute("SHOW DATABASES LIKE 'ex_officials'")
        ex_officials_db_exists = cursor.fetchone()

        if ex_officials_db_exists:
            cursor.execute("USE ex_officials")
            cursor.execute("SELECT * FROM ex_officials")
            ex_officials_records = cursor.fetchall()
            print("\nEX-OFFICIALS Database:")
            for record in ex_officials_records:
                print(record)

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        cursor.close()
        conn.close()

# Function to register past EXCO into EX-OFFICIALS
def register_past_exco():
    matric_no = int(input("Enter Matric No of past EXCO: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    office = input("Enter Office: ")
    register_exco(matric_no, name, department, office, from_ex_excos=True)

# Main program
if __name__ == "__main__":
    # Create the 'excos' and 'ex_excos' databases and tables
    create_databases_and_tables()

    while True:
        print("\nOptions:")
        print("1. Register New EXCO")
        print("2. Display Databases")
        print("3. Register Past EXCO into EX-OFFICIALS")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            matric_no = int(input("Enter Matric No: "))
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            office = input("Enter Office: ")
            register_exco(matric_no, name, department, office)
        elif choice == '2':
            display_databases()
        elif choice == '3':
            register_past_exco()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select again.")
