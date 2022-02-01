from db import connection, sql


def get_dump():
    query = "select * from users"

    result = sql.execute(query)
    rows = result.fetchall()
        
    dump_output = []

    dump_output.append('TABLE: users')
    dump_output.append('============')

    for row in rows:
        dump_output.append(row)

    dump_output.append('============')
    dump_output.append('')
    
    return dump_output
