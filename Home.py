from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Registration.db'
db = SQLAlchemy(app)


class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, unique=False)
    last_name = db.Column(db.Text, unique=False)


@app.route('/', methods=['GET'])
def registration():
    return render_template('head.html')


@app.route('/list/', methods=['GET', 'POST'])
@app.route('/list', methods=['GET', 'POST'])
def registration_1():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        if first_name == None and last_name == None:
            reg = Registration(first_name=first_name, last_name=last_name)
            db.session.add(reg)
            db.session.commit()
            return redirect(url_for('users'))
        else:
            return redirect(url_for('registration'))
    else:
        return redirect(url_for('users'))


@app.route('/list/users', methods=['GET'])
def users():
    write = Registration.query.all()
    return render_template('list.html', reg=write)


if __name__ == '__main__':
    app.run(debug=True)
