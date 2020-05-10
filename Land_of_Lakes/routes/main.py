from flask import Blueprint, render_template
from ..forms import TablesForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/search_database', methods=['GET', 'POST'])
def search_database():
    return render_template('search_database.html')


@main.route('/view_tables', methods=['GET', 'POST'])
def view_tables():

    form = TablesForm()

    if form.validate_on_submit():
        print(form.data)  # used for debugging

    return render_template('view_tables.html', form=form)
