import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute("""
    insert into task
    values(4, 1, 'write about sqlite3', 'active', '2010-10-17', 'None', 'pymotw')
    """)