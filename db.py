import sqlite3
connection = sqlite3.connect('database/points.db', check_same_thread=False)
sql = connection.cursor()

def create_tables():

    query = '''

    Create table if not exists users(
        user_id integer primary key autoincrement,
        name text,
        username text,
        password text,
        email text,
        role int,
        avatar text
    );


    '''

    sql.execute(query)


    query = '''

    Create table if not exists chores(
        chore_id integer primary key autoincrement,
        name text,
        description text,
        points text
    );


    '''

    sql.execute(query)
    
