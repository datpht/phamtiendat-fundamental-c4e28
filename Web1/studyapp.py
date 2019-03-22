from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.route('/about_me')
def about_me():
    about_me = {
        'name':'Đạt',
        'age':'18',
        'school':'HUST',
        'hobbie':'chilling'
    }
    return render_template('aboutme.html',about_me=about_me)
@app.route('/school')
def school():
    return redirect('http://techkids.vn')
if __name__=='__main__':
    app.run(debug=True)
   