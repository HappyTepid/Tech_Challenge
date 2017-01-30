# Candidate number 2005

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, required, Regexp

app = Flask(__name__)
app.secret_key = 'skdjgsgdf8duh80bt8e8hg09resj9e'

class grantApplication(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired(), Regexp('^(GIR ?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW]) ?[0-9][ABD-HJLNP-UW-Z]{2})$', message="Please enter a valid UK postcode!")])
    money_amount = StringField('How much money?', validators=[DataRequired()])
    deliciousness = TextAreaField('Why will your new cheese be most delicious?', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = grantApplication()
    if form.validate_on_submit():
        return render_template('confirmation.html')
    else:
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8080"),
        debug=True
    )
