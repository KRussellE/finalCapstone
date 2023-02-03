import sqlite3  # Utility module for working with Database

def create_table():
    conn = sqlite3.connect("programming.db")    # connect to the database
    c = conn.cursor()
    try:
        c.execute("CREATE TABLE python_programming (id INTEGER, name TEXT, grade INTEGER)") # Create a table (if not exists) called python_programming
    except sqlite3.OperationalError:
        print("The database already exists.")
        exit()    # Exit
    print("Table created!")
    conn.close()    # Close the connection

def insert_data():
    conn = sqlite3.connect("programming.db")    # Connect to the database
    c = conn.cursor()
    # Insert new rows
    c.execute("INSERT INTO python_programming VALUES (55, 'Carl Davis', 61)")
    c.execute("INSERT INTO python_programming VALUES (66, 'Dennis Fredrickson', 88)")
    c.execute("INSERT INTO python_programming VALUES (77, 'Jane Richards', 78)")
    c.execute("INSERT INTO python_programming VALUES (12, 'Peyton Sawyer', 45)")
    c.execute("INSERT INTO python_programming VALUES (2, 'Lucas Brooke', 99)")
    print("Data inserted!")
    conn.commit()   # Commit changes
    conn.close()    # Close the connection

def update_data():
    conn = sqlite3.connect("programming.db")    # Connect to the database
    c = conn.cursor()
    c.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'") # Update Carl Davis's grade to 65.
    print("Carl Davis's grade updated!")
    c.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")   # Delete Dennis Fredrickson's row.
    print("Dennis Fredrickson's row deleted!")
    c.execute("UPDATE python_programming SET grade = grade + 10 WHERE id < 55") # Change the grade of all people with an id below than 55
    print("Grades updated!")
    conn.commit()   # Commit changes
    conn.close()    # Close the connection

def select_data():
    conn = sqlite3.connect("programming.db")    # Connect to the database
    c = conn.cursor()
    c.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80") # Select all records with a grade between 60 and 80
    rows = c.fetchall()
    for row in rows:
        print(row)    
    conn.close()    # Close the connection

if __name__ == '__main__':
    create_table()
    insert_data()
    select_data()
    update_data()