<h1 align="center">
    Customers with location using GoogleAPI
</h1>
<p align="center">🚀 Checking data location by customer city 🚀</p>

##Preparing The environment:
Configuring environment

    pip install virtualenv

    virtualenv .venv
    
    source .venv/bin/activate
    
    pip install -r requirements.txt
I put my Apikey in .env file, but if you prefer use your own ApyKey just change in .env

##How To Run:

    1 - make install
    2 - make run
    3 - make user (to creating a super user)

Access the http://localhost:8000/admin/customer/customer/ have no customers
 
 In root of the project I put the 'customers.csv' <br >
 now, to import it, run the command: 
 
    make extract
It taking about 4 minutes to extract all the customers, because I don't found a way to get a list in Api.<br>
Then I take the list, make a get one by one and build a dict.<br>
If you want to run another csv write 'docker-compose exec web bash -c 'python manage.py customers_bulkupsert --path'
##Api:
###Documentation: http://127.0.0.1:8000/documentation/
Endpoints:
Get all customers (you can see in the browser too): http://127.0.0.1:8000/customers/

Get By id: http://127.0.0.1:8000/customers/{id}
###Tests:

In 'customer/tests/management/command/tests_customer_bulkupsert.py' we have the tests to run the tests just run command

    make test
 