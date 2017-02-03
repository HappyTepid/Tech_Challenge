# Candidate number 2005

from flask import Flask, render_template, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, required, Regexp
from flask_sqlalchemy import SQLAlchemy
import os
import re

base_path = os.getcwd()
db_path = os.path.join(base_path, 'TechChallenge.db')

app = Flask(__name__)
app.secret_key = 'skdjgsgdf8duh80bt8e8hg09resj9e'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///'+str(db_path)

db = SQLAlchemy(app)

class Submissions(db.Model):
    ID = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    FIRST_NAME = db.Column(db.Text, nullable=False)
    LAST_NAME = db.Column(db.Text, nullable=False)
    POSTCODE = db.Column(db.String(10), nullable=False)
    AMOUNT = db.Column(db.Float, nullable=False)
    REASON = db.Column(db.Text, nullable=False)

    def __init__(self, ID, FIRST_NAME, LAST_NAME, POSTCODE, AMOUNT, REASON):
        self.ID = ID
        self.FIRST_NAME = FIRST_NAME
        self.LAST_NAME = LAST_NAME
        self.POSTCODE = POSTCODE
        self.AMOUNT = AMOUNT
        self.REASON = REASON

    def __repr__(self):
        return '<Submission %r>' % self.ID

class grantApplication(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired(), Regexp('^(GIR ?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW]) ?[0-9][ABD-HJLNP-UW-Z]{2})$', flags=re.IGNORECASE, message="Please enter a valid UK postcode!")])
    money_amount = StringField('How much money do you need?', validators=[DataRequired(), Regexp('^([0-9]+(\.[0-9]+)?|\.[0-9]+)$', message="Please enter a numeric amount")])
    deliciousness = TextAreaField('Why will your new cheese be most delicious?', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = grantApplication()
    if form.validate_on_submit():
        submission = Submissions(None, str(form.first_name.data), str(form.last_name.data), str(form.postcode.data), float(form.money_amount.data), str(form.deliciousness.data))
        db.session.add(submission)
        db.session.commit()
        session['name'] = form.first_name.data
        return redirect('confirmation')
    else:
        return render_template('index.html', form=form)

@app.route('/confirmation')
def confirmation():
    if session.get('name'):
        return render_template('confirmation.html', name=session['name'])
    else:
        return redirect('/')

@app.route('/submissions')
def submissions():
    rows = Submissions.query.order_by(Submissions.ID.desc()).all()
    return render_template('submissions.html', rows=rows)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8080"),
        debug=True
    )
