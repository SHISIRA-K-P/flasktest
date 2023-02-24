from flask import Flask,render_template,redirect,url_for,request,flash
app = Flask(__name__)

@app.route('/test',methods=["GET"])
def createUser(): 
    return "Hi, I am using pythonanywhere"
    
if __name__ == "__main__":
    with app.app_context():
        app.run(host='0.0.0.0',port=5003,debug = True)



# 1.pythonanywhere a/c
# 2.git hub
