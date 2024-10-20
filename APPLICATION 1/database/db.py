# database/db.py

import sqlite3

def init_db():
    """Initialize the database and create tables if they don't exist."""
    try:
        conn = sqlite3.connect('rules.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS rules (
                rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
                rule_string TEXT NOT NULL,
                ast TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
    finally:
        conn.close()

def add_rule(rule_string, ast):
    """Add a new rule to the database."""
    try:
        conn = sqlite3.connect('rules.db')
        c = conn.cursor()
        c.execute('INSERT INTO rules (rule_string, ast) VALUES (?, ?)', (rule_string, ast))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding rule: {e}")
    finally:
        conn.close()

def get_rules():
    """Retrieve all rules from the database."""
    try:
        conn = sqlite3.connect('rules.db')
        c = conn.cursor()
        c.execute('SELECT * FROM rules')
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error retrieving rules: {e}")
        return []
    finally:
        conn.close()

def delete_rule(rule_id):
    """Delete a rule from the database by rule_id."""
    try:
        conn = sqlite3.connect('rules.db')
        c = conn.cursor()
        c.execute('DELETE FROM rules WHERE rule_id = ?', (rule_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting rule: {e}")
    finally:
        conn.close()

def update_rule(rule_id, new_rule_string, new_ast):
    """Update an existing rule in the database."""
    try:
        conn = sqlite3.connect('rules.db')
        c = conn.cursor()
        c.execute('UPDATE rules SET rule_string = ?, ast = ? WHERE rule_id = ?', 
                  (new_rule_string, new_ast, rule_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating rule: {e}")
    finally:
        conn.close()
