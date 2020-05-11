from flask import Blueprint, render_template

from ..forms import (ClientForm, AdvisorForm, OneAccountForm, TwoAccountForm,
                     UpdateClient, DeleteForm, HowManyAccountsForm)

add = Blueprint('add', __name__)


@add.route('/add_client', methods=['GET', 'POST'])
def add_client():

    form = ClientForm()

    if form.validate_on_submit():

        ssn = form.ssn.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        city = form.city.data
        state = form.state.data
        house_number = form.house_number.data
        zip_code = form.zip_code.data
        email = form.email.data

        print('Info from Forms')
        print('---------------')
        print("ssn: " + str(ssn))
        print("first_name: " + str(first_name))
        print("last_name: " + str(last_name))
        print("city: " + str(city))
        print("state: " + str(state))
        print("house_number: " + str(house_number))
        print("zip_code: " + str(zip_code))
        print("email: " + str(email))

    return render_template('add_client.html', form=form)


@add.route('/add_advisor', methods=['GET', 'POST'])
def add_advisor():

    form = AdvisorForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        area_of_expertise = form.expertise.data

        print('Info from Forms')
        print('---------------')
        print("first_name: " + str(first_name))
        print("last_name: " + str(last_name))
        print("area_of_expertise: " + str(area_of_expertise))

    return render_template('add_advisor.html', form=form)


@add.route('/add_account', methods=['GET', 'POST'])
def add_account():

    how_many_form = HowManyAccountsForm()
    one_form = OneAccountForm()
    two_form = TwoAccountForm()

    if how_many_form.validate_on_submit():
        num_wanted = how_many_form.number_wanted.data
        print("Client wants " + str(num_wanted) + " account owners")

        return render_template('add_account.html',
                               how_many_form=how_many_form,
                               num_wanted=num_wanted, one_form=one_form,
                               two_form=two_form)

    if one_form.validate_on_submit():
        id = one_form.id.data

        print('Info from Forms')
        print('---------------')
        print("client_id: " + str(id))

    if two_form.validate_on_submit():
        id_one = two_form.id_one.data
        id_two = two_form.id_two.data

        print('Info from Forms')
        print('---------------')
        print("id_one: " + str(id_one))
        print("id_two: " + str(id_two))

    return render_template('add_account.html', how_many_form=how_many_form)


@add.route('/update_client', methods=['GET', 'POST'])
def update_client():

    form = UpdateClient()
    if form.validate_on_submit():
        id = form.id.data
        ssn = form.ssn.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        city = form.city.data
        state = form.state.data
        house_number = form.house_number.data
        zip_code = form.zip_code.data
        email = form.email.data

        print('Info from Forms')
        print('---------------')
        print("id: " + str(id))
        print("ssn: " + str(ssn))
        print("first_name: " + str(first_name))
        print("last_name: " + str(last_name))
        print("city: " + str(city))
        print("state: " + str(state))
        print("house_number: " + str(house_number))
        print("zip_code: " + str(zip_code))
        print("email: " + str(email))

    return render_template('update_client.html', form=form)


@add.route('/delete_client', methods=['GET', 'POST'])
def delete_client():

    form = DeleteForm()
    if form.validate_on_submit():
        id = form.id.data

        print('Info from Forms')
        print('---------------')
        print("client_id: " + str(id))

    return render_template('delete_client.html', form=form)
