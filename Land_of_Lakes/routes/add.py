from flask import Blueprint, render_template

from ..forms import (ClientForm, AdvisorForm, AccountForm, UpdateClient,
                     DeleteForm)

add = Blueprint('add', __name__)


@add.route('/add_client', methods=['GET', 'POST'])
def add_client():

    form = ClientForm()

    return render_template('add_client.html', form=form)


@add.route('/add_advisor', methods=['GET', 'POST'])
def add_advisor():

    form = AdvisorForm()

    return render_template('add_advisor.html', form=form)


@add.route('/add_account', methods=['GET', 'POST'])
def add_account():

    form = AccountForm()

    return render_template('add_account.html', form=form)


@add.route('/update_client', methods=['GET', 'POST'])
def update_client():

    form = UpdateClient()

    return render_template('update_client.html', form=form)


@add.route('/delete_client', methods=['GET', 'POST'])
def delete_client():

    form = DeleteForm()

    return render_template('delete_client.html', form=form)
