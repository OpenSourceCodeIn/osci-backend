'''
db.py - database handler for recodein
currently provides dummy functions
'''

import sqlite3
class DuplicateError(Exception):
    pass

def add_student(username, name, email, password, confcode):
    conn = sqlite3.connect('recodein.db')
    c = conn.cursor()
    try:
        c.execute('insert into unconfirmed_students values ( ?, ?, ?, ?, ? )', (username, name, email, password, confcode,))
        conn.commit()
    except sqlite3.IntegrityError as e:
        if 'UNIQUE constraint failed' in str(e):
            conn.close()
            raise DuplicateError from e
    print(f'''Added student with username '{username}', name '{name}', email '{email}', and password '{password}'. Confirmation code is '{confcode}'.''')
    conn.close()

def add_mentor(email, org):
    conn = sqlite3.connect('recodein.db')
    c = conn.cursor()
    try:
        c.execute('insert into unconfirmed_mentors values ( ?, ? )', (email, org))
        conn.commit()
    except sqlite3.IntegrityError as e:
        if 'UNIQUE constraint failed' in str(e):
            conn.close()
            raise DuplicateError from e
    print(f'''Added mentor with email '{email}' and org '{org}'.''')
