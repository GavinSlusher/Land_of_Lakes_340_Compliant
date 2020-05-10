from flask import Blueprint, render_template

# from ..forms import (ClientForm, AdvisorForm, AccountForm, UpdateClient,
                     # DeleteForm, TablesForm)

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/search_database', methods=['GET', 'POST'])
def search_database():
    return "search database"

@main.route('/view_tables', methods=['GET', 'POST'])
def view_tables():
    return "view_tables"
