from db import connection, sql


#CREATE user
def user_create(name, username, password, email, avatar):

    query='''
    INSERT into users (name, username, password, email, avatar) 
    VALUES (?,?,?,?,?);
    '''
    sql.execute(query, [name, username, password, email, avatar])
    connection.commit()

#RETRIEVE user


#UPDATE user


#DELETE user


#CREATE TEST DATA
def insert_test_data():
    #user_create("Skippy","skipster","123","sk@aol.com","http://")
    #user_create("Charley","charles","123","ch@aol.com","http://")
    #user_create("Princess","pinky","123","pi@aol.com","http://")
    #user_create("Elly","ellen","123","el@aol.com","http://")
    #user_create("codey12","cody","123","co@aol.com","http://")
    #user_create("abber","abby","123","ab@aol.com","http://")