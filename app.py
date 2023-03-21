import sqlite3
from datetime import datetime

def create_project(name, description, created_by):
    conn = sqlite3.connect('eco_dada.db')
    c = conn.cursor()
    now = datetime.now()
    date_created = now.strftime("%Y-%m-%d %H:%M:%S")
    c.execute('INSERT INTO projects (name, description, date_created, created_by) VALUES (?, ?, ?, ?)',
              (name, description, date_created, created_by))
    project_id = c.lastrowid
    conn.commit()
    conn.close()
    return project_id
