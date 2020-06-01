from flask import Blueprint, render_template
from ..db_connector.db_connector import connect_to_database, execute_query
from ..forms import (ClientForm, AdvisorForm, OneAccountForm, TwoAccountForm,
                     UpdateClient, DeleteForm, HowManyAccountsForm, AskIfNull, UpdateClientAddress)

add = Blueprint('add', __name__)

def optional_data(form_request):
    if form_request:
        data = form_request
    else:
        data = "NULL"
    
    return data


@add.route('/add_client', methods=['GET', 'POST'])
def add_client():

    db_connection = connect_to_database()

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

        # This will insert the form data into the addresses table
        address_query = (f"INSERT INTO `addresses` (`city`, `state`,\
                                `house_number`, `zip_code`)\
                           VALUES ('{city}', '{state}', '{house_number}',\
                                '{zip_code}');")

        execute_query(db_connection, address_query)

        # This will grab the most recent address_id added to the addresses
        get_address = "SELECT address_id FROM addresses ORDER BY address_id\
                       DESC LIMIT 1;"

        address_id = execute_query(db_connection, get_address).fetchall()
        address_id = address_id[0][0]
        print(address_id)

        # Insert into the client table
        client_query = (f"INSERT INTO `clients`(`ssn`, `first_name`,\
                            `last_name`, `email`, `address_id`)\
                        VALUES ('{ssn}', '{first_name}', '{last_name}',\
                            '{email}', '{address_id}');")

        execute_query(db_connection, client_query)

    return render_template('add_client.html', form=form)


@add.route('/add_advisor', methods=['GET', 'POST'])
def add_advisor():

    db_connection = connect_to_database()

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

        advisor_query = (f"INSERT INTO `financial_advisors` (`first_name`,\
                            `last_name`, `area_of_expertise`)\
                          VALUES ('{first_name}', '{last_name}',\
                            '{area_of_expertise}');")

        print(advisor_query)

        execute_query(db_connection, advisor_query)

    return render_template('add_advisor.html', form=form)


@add.route('/add_account', methods=['GET', 'POST'])
def add_account():

    db_connection = connect_to_database()

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
        client_id = one_form.id.data

        print('Info from Forms')
        print('---------------')
        print("client_id: " + str(client_id))

        # default balance to $0
        balance = 0

        # Add a new account for one, single client
        accounts_query = (f"INSERT INTO `accounts` (`balance`)\
                          VALUES ('{balance}');")

        execute_query(db_connection, accounts_query)

        get_account = "SELECT account_id FROM accounts ORDER BY account_id\
                       DESC LIMIT 1;"

        account_id = execute_query(db_connection, get_account).fetchall()
        account_id = account_id[0][0]
        print(account_id)

        # connect the account to the client

        connection_query = (f"INSERT INTO `clients_accounts` (`client_id`, `account_id`)\
                            VALUES ('{client_id}', '{account_id}');")

        execute_query(db_connection, connection_query)

    if two_form.validate_on_submit():
        id_one = two_form.id_one.data
        id_two = two_form.id_two.data

        print('Info from Forms')
        print('---------------')
        print("id_one: " + str(id_one))
        print("id_two: " + str(id_two))
        # default balance to $0
        balance = 0

        # Add a new account for one, single client
        accounts_query = (f"INSERT INTO `accounts` (`balance`)\
                          VALUES ('{balance}');")

        execute_query(db_connection, accounts_query)

        get_account = "SELECT account_id FROM accounts ORDER BY account_id\
                       DESC LIMIT 1;"

        account_id = execute_query(db_connection, get_account).fetchall()
        account_id = account_id[0][0]
        print(account_id)

        # connect the account to the client

        connection_query = (f"INSERT INTO `clients_accounts` (`client_id`, `account_id`)\
                            VALUES ('{id_one}', '{account_id}');")

        execute_query(db_connection, connection_query)

        connection_query = (f"INSERT INTO `clients_accounts` (`client_id`, `account_id`)\
                            VALUES ('{id_two}', '{account_id}');")

        execute_query(db_connection, connection_query)

    return render_template('add_account.html', how_many_form=how_many_form)


@add.route('/update_client', methods=['GET', 'POST'])
def update_client():

    db_connection = connect_to_database()

    make_null_form = AskIfNull()
    update_client_only_form = UpdateClient()
    update_client_address_form = UpdateClientAddress()

    if make_null_form.validate_on_submit():
        make_null = make_null_form.make_null.data
        print(make_null)

        return render_template('update_client.html',
                               make_null_form=make_null_form,
                               make_null=make_null, 
                               update_client_address_form=update_client_address_form,
                               update_client_only_form=update_client_only_form)

    
    # else:
    #     id = form.id.data
    #     ssn = form.ssn.data
    #     first_name = form.first_name.data
    #     last_name = form.last_name.data
    #     email = form.email.data
    #     city = form.city.data
    #     state = form.state.data
    #     house_number = form.house_number.data
    #     zip_code = form.zip_code.data
        # make_null = check_value_from_form

        # if make_null is true and address ID is None: (IE setting a null address to null)
            # error message that their address is already null
            # return redirect

        # if make_null and addressID: (null address id in clients and it is not currently null)
            # set the address to null
            
        # update address properties ()

        

        # print('Info from Forms')
        # print('---------------')
        # print("id: " + str(id))
        # print("ssn: " + str(ssn))
        # print("first_name: " + str(first_name))
        # print("last_name: " + str(last_name))
        # print("city: " + str(city))
        # print("state: " + str(state))
        # print("house_number: " + str(house_number))
        # print("zip_code: " + str(zip_code))
        # print("email: " + str(email))

        # get_address = f"SELECT address_id FROM clients WHERE client_id={id};"
            
        # address_id = execute_query(db_connection, get_address).fetchall()
        
        # print(address_id)
        # address_id = address_id[0][0]
        # print(address_id)

        # client_query = (f"UPDATE `clients`\
        #           SET\
        #                   `ssn` = {ssn},\
        #                   `first_name` = '{first_name}',\
        #                   `last_name` = '{last_name}',\
        #                   `email` = '{email}'\
        #           WHERE\
        #                   `client_id` = {id};")

        # address_query = (f"UPDATE `addresses`\
        #           SET\
        #                   `city` = '{city}',\
        #                   `state` = '{state}',\
        #                   `house_number` = {house_number},\
        #                   `zip_code` = {zip_code}\
        #           WHERE\
        #                   `address_id` = {address_id};")

        # execute_query(db_connection, client_query)
        # execute_query(db_connection, address_query)

    return render_template('update_client.html', make_null_form=make_null_form)


@add.route('/delete_account', methods=['GET', 'POST'])
def delete_account():

    db_connection = connect_to_database()

    form = DeleteForm()
    if form.validate_on_submit():
        account_id = form.id.data

        print('Info from Forms')
        print('---------------')
        print("account_id: " + str(id))

        delete_query = (f"DELETE FROM `accounts`\
                          WHERE `account_id` = {account_id};")

        execute_query(db_connection, delete_query)


    return render_template('delete_account.html', form=form)
