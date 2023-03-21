import sqlite3

def create_db():
    conn = sqlite3.connect('eco_dada.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  email TEXT UNIQUE,
                  password TEXT,
                  is_admin INTEGER DEFAULT 0)''')

    c.execute('''CREATE TABLE IF NOT EXISTS projects
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  description TEXT,
                  date_created TEXT,
                  created_by INTEGER,
                  FOREIGN KEY(created_by) REFERENCES users(id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS project_members
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  project_id INTEGER,
                  FOREIGN KEY(user_id) REFERENCES users(id),
                  FOREIGN KEY(project_id) REFERENCES projects(id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS activities
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  description TEXT,
                  date_created TEXT,
                  project_id INTEGER,
                  created_by INTEGER,
                  FOREIGN KEY(project_id) REFERENCES projects(id),
                  FOREIGN KEY(created_by) REFERENCES users(id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS comments
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  content TEXT,
                  date_created TEXT,
                  activity_id INTEGER,
                  user_id INTEGER,
                  FOREIGN KEY(activity_id) REFERENCES activities(id),
                  FOREIGN KEY(user_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()
