import sqlite3
from datetime import datetime

DB_NAME = "grievances.db"

def setup_database():
    """
    Creates the grievances table if it doesn't already exist.
    Fields match requirement F3.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grievances (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        address TEXT,
        grievance_text TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    print("Database setup complete.")

def insert_grievance(name, phone, address, grievance):
    """
    Inserts a new grievance record into the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Generate timestamp
    timestamp = datetime.now().isoformat()
    
    try:
        cursor.execute("""
        INSERT INTO grievances (name, phone_number, address, grievance_text, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """, (name, phone, address, grievance, timestamp))
        
        conn.commit()
        # Get the ID of the inserted row
        grievance_id = cursor.lastrowid
        conn.close()
        return grievance_id
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.close()
        return None