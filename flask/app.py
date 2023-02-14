from flask import Flask, request, render_template, flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column("Car #",db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable = False)
    model = db.Column(db.String(100), nullable = False)
    year = db.Column(db.String(100), nullable = False)
    price = db.Column(db.String(100), nullable = False)
    def __init__(self, make,model,year,price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
    
    def __repr__(self):
        return '<Car %r>' % self.id

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="POST":
        make_name = request.form['make']
        model_name = request.form['model']
        year_date = request.form['year']
        price_point = request.form['price']
        new_car = Car(make_name, model_name, year_date,price_point)
        try:
            db.session.add(new_car)
            db.session.commit()
            redirect('/')
        except: 
            return('There was an issue adding this') 
    else:
        cars = Car.query.order_by(Car.year_date).all()
        return render_template("index.html", cars=cars)
    


if __name__ == '__main__':
    app.run(debug=False)
    
