from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField

from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class ClientForm(FlaskForm):
    ssn = IntegerField("Client's SSN: ", validators=[DataRequired()])
    first_name = StringField("First Name: ", validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    city = StringField("City: ")
    state = StringField('State: ')
    house_number = IntegerField("House Number: ")
    zip_code = IntegerField('Zip Code: ')
    email = EmailField('Email: ')
    submit = SubmitField("Submit")


class AdvisorForm(FlaskForm):
    first_name = StringField("First Name: ")
    last_name = StringField("Last Name: ")
    expertise = SelectField("Area of Expertise: ",
                            choices=[('tax', 'Taxation'),
                                     ('estate', 'Estate Planning'),
                                     ('portfolio', 'Portfolio Management')])
    submit = SubmitField("Submit")


class UpdateClient(FlaskForm):
    id = IntegerField("Client's ID: ", validators=[DataRequired()])
    ssn = IntegerField("Client's SSN: ", validators=[DataRequired()])
    first_name = StringField("First Name: ", validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    city = StringField("City: ")
    state = StringField('State: ')
    house_number = IntegerField("House Number: ")
    zip_code = IntegerField('Zip Code: ')
    email = EmailField('Email: ')
    submit = SubmitField("Submit")


class AccountForm(FlaskForm):
    id = IntegerField("Client's ID: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class DeleteForm(FlaskForm):
    id = IntegerField("Client's ID: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class TablesForm(FlaskForm):
    tables = SelectField("Select Table: ",
                         choices=[('clients', 'Clients'),
                                  ('accounts', 'Accounts'),
                                  ('clients_advisors', 'Clients Advisors'),
                                  ('clients_accounts', 'Clients Accounts'),
                                  ('addresses', 'Addresses'),
                                  ('financial_advisors',
                                   'Financial Advisors')])

    submit = SubmitField("Submit")
