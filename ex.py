import mysql.connector

# Function to create the 'nacos-excos' database and tables if they don't exist
def create_database_and_tables():
    conn = mysql.connector.connect(
        host="localhost",
            user="tester",
            password="test"
    )
    
    cursor = conn.cursor()
    
    # Create the 'nacos-excos' database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS nacos_excos")
    cursor.execute("USE nacos_excos")

    # Create the 'excos' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS excos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            department VARCHAR(255),
            office VARCHAR(255),
            matric_no VARCHAR(255) UNIQUE
        )
    """)

    # Create the 'ex-excos' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ex_excos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            department VARCHAR(255),
            office VARCHAR(255),
            matric_no VARCHAR(255) UNIQUE
        )
    """)

    conn.commit()
    conn.close()

# Function to add a new record to the 'excos' table
def add_exco(name, department, office, matric_no):
    conn = mysql.connector.connect(
        host="localhost",
            user="tester",
            password="test",
        database="nacos_excos"
    )

    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO excos (name, department, office, matric_no)
            VALUES (%s, %s, %s, %s)
        """, (name, department, office, matric_no))
        conn.commit()
        print("Exco added successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        conn.close()

# Function to transfer records from 'excos' to 'ex-excos' based on office
def transfer_records_by_office():
    conn = mysql.connector.connect(
        host="localhost",
            user="tester",
            password="test",
        database="nacos_excos"
    )

    cursor = conn.cursor()

    try:
        # Select offices with more than one record in 'excos' table
        cursor.execute("""
            SELECT office
            FROM excos
            GROUP BY office
            HAVING COUNT(office) > 1
        """)

        offices_to_transfer = [row[0] for row in cursor.fetchall()]

        for office in offices_to_transfer:
            # Select records to transfer
            cursor.execute("""
                SELECT name, department, office, matric_no
                FROM excos
                WHERE office = %s
            """, (office,))

            records_to_transfer = cursor.fetchall()

            # Insert records into 'ex_excos' table
            for record in records_to_transfer:
                cursor.execute("""
                    INSERT INTO ex_excos (name, department, office, matric_no)
                    VALUES (%s, %s, %s, %s)
                """, record)

            # Delete records from 'excos' table
            cursor.execute("""
                DELETE FROM excos
                WHERE office = %s
            """, (office,))
        
        conn.commit()
        print("Records transferred successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        conn.close()


# Function to display both 'excos' and 'ex-excos' tables
def display_tables():
    conn = mysql.connector.connect(
        host="localhost",
            user="tester",
            password="test",
        database="nacos_excos"
    )

    cursor = conn.cursor()

    # Display 'excos' table
    cursor.execute("SELECT * FROM excos")
    print("Excos Table:")
    for row in cursor.fetchall():
        print(row)

    # Display 'ex-excos' table
    cursor.execute("SELECT * FROM ex_excos")
    print("\nEx-Excos Table:")
    for row in cursor.fetchall():
        print(row)

    conn.close()

# Main function
if __name__ == "__main__":
    create_database_and_tables()

    while True:
        print("\nCreated by Group A")
        print("\nNACOS-EXCOS App Menu:")
        
        print("1. Add New Exco")
        print("2. Transfer Records to Ex-Excos")
        print("3. Display Tables")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            department = input("Enter department: ")
            office = input("Enter office: ")
            matric_no = input("Enter matric number: ")
            add_exco(name, department, office, matric_no)
        elif choice == "2":
            transfer_records_by_office()
        elif choice == "3":
            display_tables()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")
