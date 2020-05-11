from flask import Blueprint, render_template
from ..forms import TablesForm
from ..db_connector.db_connector import connect_to_database, execute_query

main = Blueprint('main', __name__)


@main.route('/')
def index():

    # Testing db_connection

    db_connection = connect_to_database()
    query = ("SELECT id, fname, lname, homeworld, age FROM bsg_people "
             "ORDER BY id;")

    print(query)

    rows = execute_query(db_connection, query).fetchall()
    print(rows)

    return render_template('index.html', rows=rows)


@main.route('/search_database', methods=['GET', 'POST'])
def search_database():
    return render_template('search_database.html')


@main.route('/view_tables', methods=['GET', 'POST'])
def view_tables():

    form = TablesForm()

    if form.validate_on_submit():
        print(form.data)  # used for debugging

    return render_template('view_tables.html', form=form)
