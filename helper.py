import cgi, json

def create_json(cursor):
    headers = list(map(lambda x: x[0], cursor.description))
    results = []
    output = {}

    for row in cursor.fetchall():
        rowData = {}
        for i, col in enumerate(row):
            rowData[headers[i]] = col
        results.append(rowData)
    if len(results):
        output['data'] = results
        output['error'] = 0
        return json.dumps(output)

def get_input():
    form_data = cgi.FieldStorage()
    if form_data:
        data = {}
        for key in form_data.keys():
            data[key] = form_data[key].value
        return data