
import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the selling tickets form. 
The tests will only test the frontend portion of the program, by patching the backend to return
specific values. For example:
@patch('qa327.backend.get_user', return_value=test_user)
Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.
Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Moch a sample user
test_user = User(
    email='jivanji_adnan@test.com',
    name='test_frontend',
    password=generate_password_hash('AdnanJivanji11$'),
    balance='5000'
    
)

# Moch some sample tickets
test_tickets = [
    {'name': 'Ticket1', 'price': '100', 'quantity': 30, 'expiration date': '20210922'}
]



class BuyFormTest(BaseCase):
    
    #This function checks whether index page shows message when ticket name is not alphanumeric
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_alphanumeric(self, *_):
        self.open(base_url + '/logout')
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "AdnanJivanji11$")
        #click enter button
        self.click('input[type="submit"]')
        # open home page
        self.open(base_url)

        #fill in ticket name that is not alphanumeric
        self.type("#buyname", "j8&*ushkmf")
        self.type("#buyquantity", "20")
        self.click("#t-submit")

        self.assert_element("#message")
        self.assert_text("name not alphanumeric", "#message")

    #This function checks whether index page shows errormessage when ticket name has spaces at beginning/end
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_spaces(self, *_):
        self.open(base_url + '/logout')
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "AdnanJivanji11$")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        #fill in ticket name that has space at start
        self.type("#buyname", " pinkpanther")
        self.type("#buyquantity", "20")
        self.click("#t-submit")

        self.assert_element("#message")
        self.assert_text("space at start/end", "#message")

    #This function checks whether index page shows errormessage when quantity is negative
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_quantity(self, *_):
        self.open(base_url + '/logout')
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "AdnanJivanji11$")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        self.type("#buyname", "pinkpanther")
        #fill negative quantity
        self.type("#buyquantity", "-1")
        self.click("#t-submit")

        self.assert_element("#message")
        self.assert_text("quantity not between 1 and 100 (inclusive)", "#message")

    #This function checks whether index page shows errormessage when quantity is greater than 100
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_quantitygt(self, *_):
        self.open(base_url + '/logout')
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "AdnanJivanji11$")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        self.type("#buyname", "pinkpanther")
        #fill quantity as 500
        self.type("#buyquantity", "500")
        self.click("#t-submit")

        self.assert_element("#message")
        self.assert_text("quantity not between 1 and 100 (inclusive)", "#message")
    
    

   
    #This function checks whether index page shows errormessage when ticketname is shorter than 60ch
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_longname(self, *_):
        self.open(base_url + '/logout')
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "AdnanJivanji11$")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        self.type("#buyname", "pinkdfjkgndfgkdgbhkcbhkcedsjgfnkebrejhbfgjrehbfdgrdhdfkhjgdfhj")
        self.type("#buyquantity", "20")
        self.click("#t-submit")

        self.assert_element("#message")
        self.assert_text("username too short or too long", "#message")
    
    #This function checks whether the ticket exists in the database
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_tickets_exists(self, *_):
        self.open(base_url + '/logout')
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "AdnanJivanji11$")
        #click enter button
        self.click('input[type="submit"]')
        # open home page
        self.open(base_url)
        self.type("#buyname", "Come On")
        self.type("#buyquantity", "2")
        self.click("#t-submit")
        self.assert_element("#message")
        self.assert_text("Sorry, this ticket is not available.", "#message")
          
    #This function checks whether the ticket exists in the database
    @patch('qa327.backend.get_user', return_value=test_user)
    #@patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_tickets_quantity(self, *_):
        self.open(base_url + '/logout')
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "AdnanJivanji11$")
        #click enter button
        self.click('input[type="submit"]')
        # open home page
        self.open(base_url)
        self.type("#tname", "Superman")
        self.type("#tquantity", "97")
        self.type("#tprice", "99")
        self.type("#texpiration", "20210319")
        self.click("#sell-btn-submit")

        self.open(base_url)
        #should open base url
        self.type("#buyname", "Superman")
        self.type("#buyquantity", "98")
        self.click("#t-submit")
        #self.open(base_url)
        #should open base url
        self.assert_element("#message")
        self.assert_text("There are not enough tickets", "#message")
    
    