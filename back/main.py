import requests
import sqlite3

con = sqlite3.connect("backup.db")
cur = con.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS Tasks (
    id TEXT,
    name TEXT,
    description TEXT,
    due_date TEXT,
    is_complated INTEGER,
    created TEXT            
    )
''')

data = requests.get("https://67877325c4a42c916106c0c3.mockapi.io/task")
for task in data.json():
    id = task["id"]
    name = task["name"]
    description = task["description"]
    due_date = task["due_date"]
    is_complated = task["is_complated"]
    created = task["created"]
    cur.execute('''INSERT INTO Tasks (id, name, description, due_date, is_complated, created) 
                VALUES (?, ?, ?, ?, ?, ?)''', 
                (id, name, description, due_date, is_complated, created))
    print(f"Success backup")

con.commit()
con.close()
