from db import connection, sql

def create_tables():

    query = '''

    Create table if not exists users(
        user_id integer primary key autoincrement,
        name text,
        username text,
        password text,
        email text,
        avatar text
    );


    '''

    sql.execute(query)


    query = '''

    Create table if not exists chores(
        Speak tamil for a day text,
        Fold clothes,
        Fold clothes,
        Fold bed,
        Chess


    );


    '''

    sql.execute(query)
    


def insert_test_data(name, username, password, email, avatar):

    query='''
    INSERT into users (name, username, password, email, avatar) 
    VALUES (?,?,?,?,?);
    '''
    sql.execute(query, [name, username, password, email, avatar])
    connection.commit()

create_tables()

insert_test_data("Skippy","skipster","123","sk@aol.com","http://")
insert_test_data("Charley","charles","123","ch@aol.com","http://")
insert_test_data("Princess","pinky","123","pi@aol.com","http://")
insert_test_data("Elly","ellen","123","el@aol.com","http://")