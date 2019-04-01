from flask import *
app = Flask(__name__)
from database import bike_rental

@app.route('/all_bike')
def all_bike():
    all_bike = bike_rental.find()
    return render_template('all_bike.html',all_bike=all_bike)

@app.route('/new_bike',methods=['GET','POST'])
def new_bike():
    if request.method == "GET":
        return render_template('bike-rental.html')
    elif request.method == "POST":
        form = request.form
        model=form['model']
        dailyfee=form['dailyfee']
        image=form['image']
        year=form['year']
        new_bike = {
            'model':model,
            'dailyfee':dailyfee,
            'image':image,
            'year':year,
        }
        bike_rental.insert_one(new_bike)
        return redirect('/all_bike')
        

if __name__ == "__main__":
    app.run(debug=True)
