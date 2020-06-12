import sqlite3
conn = sqlite3.connect('''recodein.db''')
c = conn.cursor()
c.execute('''create table unconfirmed_students (
        username text primary key,
        name     text            ,
        email    text unique     ,
        password text            , 
        confcode text
    )''')
c.execute('''create table students (
        username text primary key,
        name     text            ,
        email    text unique     ,
        password text
    )''')
c.execute('''create table unconfirmed_mentors (
        email    text primary key,
        password text
    )''')
c.execute('''create table mentors (
        username text primary key,
        name     text            ,
        email    text unique     ,
        password text            ,
        org      text
    )''')
c.execute('''create table orgs (
        name      text primary key,
        londdesc  text            ,
        shortdesc text
    )''')
c.execute('''create table tasks (
        org                 text,
        name                text,
        mentors             text,
        description         text,
        current_students    text,
        completed_students  text,
        available_instances int
    )''')
conn.commit()
conn.close()
