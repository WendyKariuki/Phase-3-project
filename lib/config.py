import sqlite3
CONN = sqlite3.connect('events.db')
CURSOR = CONN.cursor()

#creating tables
def create_tables():
    sql1 = """
    CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    date TEXT NOT NULL
    );
    """
    CURSOR.execute(sql1)

    sql2 = """
    CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    event_id INTEGER NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events(id)
    );
    """
    CURSOR.execute(sql2)

    sql3 = """
    CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_number INTEGER NOT NULL,
    price INTEGER NOT NULL,
    event_id INTEGER NOT NULL ,
    participant_id INTEGER NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events(id),
    FOREIGN KEY (participant_id) REFERENCES participants(id)
    );
    """
    CURSOR.execute(sql3)
    CONN.commit()
    print("--------created tables--------")


#dropping tables
def drop_tables():
    sql = """DROP TABLE IF EXISTS events"""
    CURSOR.execute(sql)

    sql = """DROP TABLE IF EXISTS participants"""
    CURSOR.execute(sql)

    sql = """DROP TABLE IF EXISTS tickets"""
    CURSOR.execute(sql)

    CONN.commit()

# drop_tables()
create_tables()

