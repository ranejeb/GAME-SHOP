<<<<<<< HEAD
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    text = db.Column(db.Text, nullable=False )


def __repr__(self):
    return self.title



@app.route('/')
def index():  # put application's code here
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data = items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        text = request.form['text']

        item = Item(title=title, price=price, text=text)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except Exception:
            logging.exception('')
            return ''
    else:
        return render_template('create.html')
    



if __name__ == '__main__':
    app.run(debug=True) # False
=======
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    text = db.Column(db.Text, nullable=False )


def __repr__(self):
    return self.title



@app.route('/')
def index():  # put application's code here
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data = items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        text = request.form['text']

        item = Item(title=title, price=price, text=text)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except Exception:
            logging.exception('')
            return ''
    else:
        return render_template('create.html')
    



if __name__ == '__main__':
    app.run(debug=True) # False
>>>>>>> 220386cca4eb1fef487e2c9c0993d6526e8d7045
