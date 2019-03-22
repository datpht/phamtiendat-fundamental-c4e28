from flask import Flask
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    bmi = weight/((height/100)**2)
    
    if bmi < 16:
        return "Severely underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi <30:
        return "Overweight"
    else:
        return "Obese" 
   
if __name__ == "__main__":
    app.run(debug=True)