from flask import Flask,redirect,url_for,render_template,request
from dump import get_dump
from db import connection, sql, create_tables
from users import user_create, insert_test_data

app=Flask(__name__)

create_tables()
insert_test_data()

@app.route('/',methods=['GET','POST'])
def home():
    current_user="Kathirrrrrrrr"
    if request.method=='POST':
        # Handle POST Request here
        return render_template('home.html', user=current_user)
    return render_template('home.html', user=current_user)

@app.route('/dump',methods=['GET','POST'])
def dump():
    dump = get_dump()
    if request.method=='POST':
        # Handle POST Request here
        return render_template('dump.html', dump=dump)
    return render_template('dump.html', dump=dump)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)