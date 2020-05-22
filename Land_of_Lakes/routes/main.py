from flask import Blueprint, render_template
from ..forms import TablesForm, ConnectAdvisorForm
from ..db_connector.db_connector import connect_to_database, execute_query

main = Blueprint('main', __name__)


@main.route('/')
def index():

    return render_template('index.html')


@main.route('/connect_advisor', methods=['GET', 'POST'])
def connect_advisor():

    form = ConnectAdvisorForm()
    return render_template('connect_advisor.html', form=form)


@main.route('/search_database', methods=['GET', 'POST'])
def search_database():
    return render_template('search_database.html')


@main.route('/view_tables', methods=['GET', 'POST'])
def view_tables():
    db_connection = connect_to_database()

    form = TablesForm()

    if form.validate_on_submit():

        if form.tables.data == 'clients':
            query = ("SELECT\
                        `client_id` as 'Client ID',\
                        `ssn` as 'Social Security Number',\
                    CONCAT(`first_name`, ' ', `last_name`) as 'Client Name',\
                        `email` as 'Email'\
                     FROM\
                        `clients`;")

            rows = execute_query(db_connection, query).fetchall()

            return render_template('view_clients.html', form=form, rows=rows)

        elif form.tables.data == 'accounts':
            query = ("SELECT\
                        `account_id` as 'Account Number',\
                        `balance` as 'Account Balance'\
                     FROM\
                        `accounts`;")

            rows = execute_query(db_connection, query).fetchall()

            return render_template('view_accounts.html', form=form, rows=rows)

        elif form.tables.data == 'clients_advisors':
            query = ("SELECT\
                        `client_advisor_id` as 'Client Advisor ID',\
                        `client_id` as 'Client ID',\
                        `advisor_id` as 'Advisor ID'\
                     FROM\
                        `clients_advisors`;")

            rows = execute_query(db_connection, query).fetchall()

            return render_template('view_clients_advisors.html',
                                   form=form,
                                   rows=rows)

        elif form.tables.data == 'clients_accounts':
            query = ("SELECT\
                            `client_account_id` as 'Client Account ID',\
                            `client_id` as 'Client ID',\
                            `account_id` as 'Account ID'\
                     FROM\
                            `clients_accounts`;")

            rows = execute_query(db_connection, query).fetchall()

            return render_template('view_clients_accounts.html',
                                   form=form,
                                   rows=rows)

        elif form.tables.data == 'addresses':
            query = ("SELECT\
                            `address_id` as 'Address ID',\
                            `city` as 'City',\
                            `state` as 'State',\
                            `house_number` as 'House Number',\
                            `zip_code` as 'Zip Code'\
                    FROM\
                            `addresses`;")

            rows = execute_query(db_connection, query).fetchall()

            return render_template('view_addresses.html', form=form, rows=rows)

        elif form.tables.data == 'financial_advisors':
            #print("VEIW FINANCIAL ADVISORS")
            query = ("SELECT\
                        `advisor_id` as 'Advisor ID',\
                        `area_of_expertise` as 'Area of Expertise',\
                        `first_name` as 'First Name',\
                        `last_name` as 'Last Name'\
                    FROM\
                        `financial_advisors`;")
                        
            rows = execute_query(db_connection, query).fetchall()

            return render_template('view_financial_advisors.html', form=form, rows=rows)
            #print("They want financial advisors")

    return render_template('view_tables.html', form=form)
