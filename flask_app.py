from flask import Flask,redirect,url_for,render_template,request
from dump import get_dump

app=Flask(__name__)



@app.route('/',methods=['GET','POST'])
def home():
    dump = get_dump()
    if request.method=='POST':
        # Handle POST Request here
        return render_template('output.html')
    return render_template('output.html', dump=dump)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)