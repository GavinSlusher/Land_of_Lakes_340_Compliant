from flask import Blueprint

add = Blueprint('add', __name__)


@add.route('/add_client', methods=['GET', 'POST'])
def add_client():
    return "Add Client"


@add.route('/add_advisor', methods=['GET', 'POST'])
def add_advisor():
    return "Add Advisor"


@add.route('/add_account', methods=['GET', 'POST'])
def add_account():
    return "Add Account"


@add.route('/update_client', methods=['GET', 'POST'])
def update_client():
    return "Update Client"


@add.route('/delete_client', methods=['GET', 'POST'])
def delete_client():
    return "Delete Client"
