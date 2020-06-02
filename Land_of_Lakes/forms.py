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
                            choices=[('Taxation', 'Taxation'),
                                     ('Estate Planning', 'Estate Planning'),
                                     ('Portfolio Management',
                                      'Portfolio Management')])
    submit = SubmitField("Submit")


class ConnectAdvisorForm(FlaskForm):
    client_id = IntegerField("Client ID: ", validators=[DataRequired()])
    advisor_id = IntegerField("Advisor ID: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AskIfNull(FlaskForm):
    make_null = SelectField("Do you want to nullify the Client's Address? ",
                            choices=[('True', 'Yes'),
                                     ('False', 'No')])
    submit = SubmitField("Submit")


class UpdateClientAddress(FlaskForm):
    id = IntegerField("Client's ID: ", validators=[DataRequired()])
    ssn = IntegerField("Client's SSN: ", validators=[DataRequired()])
    first_name = StringField("First Name: ", validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    city = StringField("City: ", validators=[DataRequired()])
    state = StringField('State: ', validators=[DataRequired()])
    house_number = IntegerField("House Number: ", validators=[DataRequired()])
    zip_code = IntegerField('Zip Code: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    submit = SubmitField("Submit")


class UpdateClient(FlaskForm):
    id = IntegerField("Client's ID: ", validators=[DataRequired()])
    ssn = IntegerField("Client's SSN: ", validators=[DataRequired()])
    first_name = StringField("First Name: ", validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    submit = SubmitField("Submit")


class HowManyAccountsForm(FlaskForm):
    number_wanted = SelectField("Number of Account Owners: ",
                                choices=[('1', 'One'),
                                         ('2', 'Two')])
    submit = SubmitField("Submit")


class OneAccountForm(FlaskForm):
    id = IntegerField("Client's ID: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class TwoAccountForm(FlaskForm):
    id_one = IntegerField("First Client ID: ", validators=[DataRequired()])
    id_two = IntegerField("Second Client ID: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class DeleteForm(FlaskForm):
    id = IntegerField("Account ID: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    searched_parameter = StringField('Last Name:', validators=[DataRequired()])
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
