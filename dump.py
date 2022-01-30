from db import connection, sql


def get_dump():
    query = "select * from users"

    result = sql.execute(query)
    rows = result.fetchall()
        
    dump_output = []

    for row in rows:
        dump_output.append(row)
    
    return dump_output
