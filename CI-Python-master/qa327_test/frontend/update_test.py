import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
"""
    This file defines all unit tests for the updating tickets. 

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
    password=generate_password_hash('AdnanJivanji11$')
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]

class UpdateTest(BaseCase):

    #R5.1: This function checks whether index page shows message when ticket name is not alphanumeric
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
        self.type("#uname", "j8&*ushkmf")
        self.type("#uquantity", "20")
        self.click("#update-btn-submit")

        self.assert_element("#message")
        self.assert_text("name not alphanumeric", "#message")

    #R5.1.2: This function checks whether index page shows errormessage when ticket name has spaces at beginning/end
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
        self.type("#uname", " pinkpanther")
        self.type("#uquantity", "20")
        self.click("#update-btn-submit")

        self.assert_element("#message")
        self.assert_text("space at start/end", "#message")

#R5.2: This function checks whether index page shows errormessage when ticketname is shorter than 60ch
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
        self.type("#uname", "lol")
        self.type("#uquantity", "20")
        self.click("#update-btn-submit")

        self.assert_element("#message")
        self.assert_text("username too short or too long", "#message")

#R5.3: ???This function checks whether index page shows errormessage when quantity is greater than 100
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
        self.type("#uquantity", "500")
        self.click("#update-btn-submit")

        self.assert_element("#message")
        self.assert_text("quantity not between 1 and 100 (inclusive)", "#message")

#R5.4.1: This function checks whether index page shows errormessage when price is lt 10
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_pricelt(self, *_):
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
        self.type("#uname", "pinkpanther")
        self.type("#uquantity", "20")
        #fill price as less than 10
        self.type("#uprice", "9")
        self.type("#uexpiration", "20200901")
        self.click("#update-btn-submit")

        self.assert_element("#message")
        self.assert_text("price not in range", "#message")

#R5.4.2: This function checks whether index page shows errormessage when price is gt 100
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_pricegt(self, *_):
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
        self.type("#uname", "pinkpanther")
        self.type("#tquantity", "20")
        #fill price as greater than 100
        self.type("#uprice", "101")
        self.type("#uexpiration", "20200901")
        self.click("#update-btn-submit")

        self.assert_element("#message")
        self.assert_text("price not in range", "#message")

#R5.5: This function checks whether index page shows errormessage when date is in wrong format
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_expiration(self, *_):
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
        self.type("#uname", "pinkpanther")
        self.type("#uquantity", "20")
        self.type("#uprice", "50")
        #fill date with wrong date format
        self.type("#uexpiration", "2020")
        self.click("#update-btn-submit")

        self.assert_element("#message")
        self.assert_text("Incorrect expiration date format", "#message")

#R5.6: This function checks whether the ticket exists in the database
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
        self.type("#uname", "Come On")
        self.type("#uquantity", "2")
        self.click("#update-btn-submit")
        self.assert_element("#message")
        self.assert_text("Sorry, this ticket is not available.", "#message")
