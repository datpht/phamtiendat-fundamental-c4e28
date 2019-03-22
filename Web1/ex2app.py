from flask import Flask,render_template
app = Flask(__name__)

@app.route('/user/<username>')
def user(username):
    users = {
        "huy":{
            "name":"Nguyen Quang Huy",
            "age":29
        },
        "tuananh":{
            "name":"Huynh Tuan Anh",
            "age":22
        }
    } 
    return render_template('user.html',users=users,username=username)
if __name__ == "__main__":
    app.run(debug=True)
    