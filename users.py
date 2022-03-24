from db import connection, sql


#CREATE user
def add_user(name, username, password, email, role, avatar):
    if not name: return "No data received in add_user()"
    
    query = '''

    insert into users (name, username, password, email, role, avatar) values (?,?,?,?,?,?);
    '''

    sql.execute(query, [name, username, password, email, role, avatar])
    connection.commit()
    return "User has been added"

#RETRIEVE user


#UPDATE user


#DELETE user


#CREATE TEST DATA

def create_test_data():
    add_user("Wilhelm Singh","wsing1","12345678","wsing1@gmail.com","guest","https://cdn.pixabay.com/photo/2015/03/04/22/35/head-659652_1280.png")
    add_user("Nicole Singh","nsing1","12345678","nsing1@gmail.com","guest","https://cdn4.iconfinder.com/data/icons/ibrandify-female-user-action-icon/512/19-512.png")
    return