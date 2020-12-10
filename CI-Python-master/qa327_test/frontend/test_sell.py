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
    password=generate_password_hash('test_frontend')
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]


class SellFormTest(BaseCase):
    #This function checks whether index page shows message when ticket name is not alphanumeric
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_alphanumeric(self, *_):
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "test_frontend")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        #fill in ticket name that is not alphanumeric
        self.type("#tname", "j8&*ushkmf")
        self.type("#tquantity", "20")
        self.type("#tprice", "15")
        self.type("#texpiration", "2020-09-01")
        self.click('input[type="submit"]')

        self.assert_element("#message")
        self.assert_text("name not alphanumeric", "#message")
    
    #This function checks whether index page shows errormessage when ticket name has spaces at beginning/end
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_spaces(self, *_):
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "test_frontend")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        #fill in ticket name that has space at start
        self.type("#tname", " pinkpanther")
        self.type("#tquantity", "20")
        self.type("#tprice", "15")
        self.type("#texpiration", "2020-09-01")
        self.click('input[type="submit"]')

        self.assert_element("#message")
        self.assert_text("space at start/end", "#message")

    #This function checks whether index page shows errormessage when quantity is negative
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_quantity(self, *_):
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "test_frontend")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        self.type("#tname", "pinkpanther")
        #fill negative quantity
        self.type("#tquantity", "-1")
        self.type("#tprice", "15")
        self.type("#texpiration", "2020-09-01")
        self.click('input[type="submit"]')

        self.assert_element("#message")
        self.assert_text("quantity not between 1 and 100 (inclusive)", "#message")
    
    #This function checks whether index page shows errormessage when quantity is greater than 100
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_quantitygt(self, *_):
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "test_frontend")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        self.type("#tname", "pinkpanther")
        #fill quantity as 500
        self.type("#tquantity", "500")
        self.type("#tprice", "15")
        self.type("#texpiration", "2020-09-01")
        self.click('input[type="submit"]')

        self.assert_element("#message")
        self.assert_text("quantity not between 1 and 100 (inclusive)", "#message")
    
    #This function checks whether index page shows errormessage when price is lt 10
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_pricelt(self, *_):
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "test_frontend")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        self.type("#tname", "pinkpanther")
        self.type("#tquantity", "20")
        #fill price as less than 10
        self.type("#tprice", "9")
        self.type("#texpiration", "2020-09-01")
        self.click('input[type="submit"]')

        self.assert_element("#message")
        self.assert_text("price not in range", "#message")

    #This function checks whether index page shows errormessage when price is gt 100
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_pricegt(self, *_):
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "test_frontend")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        self.type("#tname", "pinkpanther")
        self.type("#tquantity", "20")
        #fill price as greater than 100
        self.type("#tprice", "101")
        self.type("#texpiration", "2020-09-01")
        self.click('input[type="submit"]')

        self.assert_element("#message")
        self.assert_text("price not in range", "#message")

    #This function checks whether index page shows errormessage when date is in wrong format
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_expiration(self, *_):
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "test_frontend")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        self.type("#tname", "pinkpanther")
        self.type("#tquantity", "20")
        self.type("#tprice", "50")
        #fill date with wrong date format
        self.type("#texpiration", "2020")
        self.click('input[type="submit"]')

        self.assert_element("#message")
        self.assert_text("Incorrect expiration date format", "#message")

    #This function checks whether index page shows errormessage when ticketname is shorter than 6ch
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_shortname(self, *_):
        #open login page
        self.open(base_url + '/login')
        #fill email and password
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#password", "test_frontend")
        #click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        self.type("#tname", "pink")
        self.type("#tquantity", "20")
        self.type("#tprice", "50")
        self.type("#texpiration", "2020-09-01")
        self.click('input[type="submit"]')

        self.assert_element("#message")
        self.assert_text("ticketname too short or too long", "#message")
    
    