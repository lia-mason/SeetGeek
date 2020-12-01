from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn

import string
import re #importing class re to be able to match fields to regex to place restraints
import datetime #allows to use datetime function to verify format of date

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    # verifies that password and password2 are the same
    if password != password2:
        error_message = "password1 and password2 don't match"
    #verifies that the username is between 2 and 20 characters
    elif len(name) <= 2 or len(name) >= 20:
        error_message = "username too short or too long"
    #each character of the username has to be alphanumeric or a space
    elif not all(chr.isalnum() or chr.isspace() for chr in name):
        error_message = "name not alphanumeric"
    #verifies that the password has atleast one upper and lower character and the password has length gt than 6
    elif not (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x in string.punctuation for x in password) and len(password) >= 6):
        error_message = "password doesn't meet required complexity"
    #username cannot have spaces at start or end
    elif name.startswith(" ") or name.endswith(" "):
        error_message = "space at start/end"
    #email cannot be empty
    elif len(email) < 1:
        error_message = "email field is empty"
    #verifies that the email has valid format
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        error_message = "email not valid"

    else:
        user = bn.get_user(email)
        #verifies that the email does not already exist
        if user:
            error_message = "this email has already been used"
        elif bn.register_user(email, name, password, password2,5000):
            error_message = "Failed to store user info."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('login.html', message=error_message)
    else:
        #bn.register_user(email,name,password,password2,5000)
        return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    error_message = None
#this is  to  set restrainst on the email so that it follows requirements in R1
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        error_message = "email/password format is incorrect"
#this sets restraints on the password so that it cant be less than 6 characters
    if len(password) < 6:
        error_message = 'email/password format is incorrect'
#this if is to set restraints on the password by asserting which characters can be included 
    if not (any(x.isupper() for x in password) and any(x.islower() for x in password) and len(password) >= 6):
        error_message = 'email/password format is incorrect'
    
    user = bn.login_user(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message= error_message)


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


@app.route('/sell', methods=['GET'])
def sell_get():
    return redirect('/')


@app.route('/sell', methods=['POST'])
def sell_post():
    name = request.form.get('tname')
    quantity = request.form.get('tquantity')
    price = request.form.get('tprice')
    expiration = request.form.get('texpiration')
    error_message = None

    #each character of the ticketname has to be alphanumeric or a space
    if not all(chr.isalnum() or chr.isspace() for chr in name):
        error_message = "name not alphanumeric"
    #ticketname cannot have spaces at start or end
    elif name.startswith(" ") or name.endswith(" "):
        error_message = "space at start/end"
    #verifies that the ticketname is between 6 and 60 characters
    elif len(name) < 6 or len(name) > 60:
        error_message = "username too short or too long"
    #verifies that the quantity is more than 0 and less than/equal to 100.
    elif quantity <= 0 or quantity > 100:
        error_message = "quantity not between 1 and 100 (inclusive)"
    #verifies that the price has to be of range [10,100]
    elif price < 10 or price > 100:
        error_message = "price not in range"
    #verifies date is in correct format
    elif not (datetime.datetime.strptime(date_text, '%Y-%m-%d')):
        error_message = "Incorrect expiration date format"
    if error_message:
        return render_template('/', message=error_message)
        
    return redirect('/')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner

#getting info from buy form 
@app.route('/buy', methods=['POST'])
def buy_submit():
     name = request.form.get('name')
     quantity = request.form.get('quantity')
     return redirect('/')

@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)
