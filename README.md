<h1 align="center">
    Customers with location using GoogleAPI
</h1>
<p align="center">🚀 Checking data location by customer city 🚀</p>

<h2>Important: FIRST OF ALL, PUT YOUR TOKEN GOOGLECLOUD IN .env </h2>

<h2>Preparing The environment:</h2>
Configuring environment

    pip install virtualenv

    virtualenv .venv
    
    source .venv/bin/activate
    
    pip install -r requirements.txt

<h2>How To Run:</h2>
    If you don't have the make configured in your local, 
    you can open the file make and execute the commands in your terminal
    1 - make install
    2 - make run
    3 - make user (to creating a super user)

Access the http://localhost:8000/admin/customer/customer/ have no customers
 
 In root of the project I put the 'customers.csv' <br >
 now, to import it, run the command: 
 
    make extract

It taking some seconds to extract all the customers, because I don't found a way to get a list in Api.<br>
Then I take the list, make a get one by one and build a dict.<br>
If you want to run another csv write 'docker-compose exec web bash -c 'python manage.py customers_bulkupsert --path'

<h1>Api</h1>
<h2>Documentation: http://127.0.0.1:8000/documentation/ </h2>
Endpoints:
Get all customers (you can see in the browser too): http://127.0.0.1:8000/customers/

Get By id: http://127.0.0.1:8000/customers/{id}
<h2>Tests:</h2>

In 'customer/tests/management/command/tests_customer_bulkupsert.py' we have the tests to run the tests just run command

    make test
 