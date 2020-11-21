import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend homepage.

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]


class FrontEndHomePageTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_header(self, *_):
        """
        This is a front end unit test to login to home page
        and verify if the welcome header is displayed correctly.
        """
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_frontend")
        # click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        # test for welcome header message ("Hi {username}")
        self.assert_text("Hi test_frontend", "#welcome-header")
        
     @patch('qa327.backend.get_user', return_value=test_user)
     def test_login(self, *_):
        """
        R3.1 This will test the login page and test if the user gets redirected to login page if not logged in
        """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#title")
        self.assert_text("Log in", "#title")
        
        #test that logout redirects to '/'
        URL = self.get_current_url();
        self.assert_equal(URL, base_url + '/'); 
        
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)    
    def test_show_user_balance(self, *_):
        """
        R3.3 This will test whether the user balance displays
        """
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_frontend")
        self.click('input[type="submit"]')
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_element("#ubalance")
        
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)    
    def test_all_tickets(self, *_):  
         # open login page
         self.open(base_url + '/login')
         # fill email and password
         self.type("#email", "test_frontend@test.com")
         self.type("#password", "test_frontend")
         # click enter button
         self.click('input[type="submit"]')
            
         # open home page
         self.open(base_url)
         # test if the page loads correctly
         self.assert_element("#welcome-header")
         self.assert_text("Welcome test_frontend", "#welcome-header")
         self.assert_element("#tickets")
         self.assert_text("Here are all available tickets")
        
        
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)    
    def test_buy_form(self, *_):  
         """
         This will test if buy form is displaying
         """
         # open login page
         self.open(base_url + '/login')
         # fill email and password
         self.type("#email", "test_frontend@test.com")
         self.type("#password", "test_frontend")
         # click enter button
         self.click('input[type="submit"]')

         # open home page
         self.open(base_url)
         # test if the page loads correctly
         self.assert_element("#welcome-header")

         self.assert_element("#name")
         self.type("#name")
         self.assert_element("#quantity")
         self.type("#quantity", "1")
         self.click("#t-submit")
         self.assert_element("#welcome-header")
       

#     @patch('qa327.backend.get_user', return_value=test_user)
#     @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    # def test_login_success(self, *_):
    #     """
    #     This is a sample front end unit test to login to home page
    #     and verify if the tickets are correctly listed.
    #     """
    #     # open login page
    #     self.open(base_url + '/login')
    #     # fill email and password
    #     self.type("#email", "test_frontend@test.com")
    #     self.type("#password", "test_frontend")
    #     # click enter button
    #     self.click('input[type="submit"]')
    #
    #     # after clicking on the browser (the line above)
    #     # the front-end code is activated
    #     # and tries to call get_user function.
    #     # The get_user function is supposed to read data from database
    #     # and return the value. However, here we only want to test the
    #     # front-end, without running the backend logics.
    #     # so we patch the backend to return a specific user instance,
    #     # rather than running that program. (see @ annotations above)
    #
    #
    #     # open home page
    #     self.open(base_url)
    #     # test if the page loads correctly
    #     self.assert_element("#welcome-header")
    #     self.assert_text("Welcome test_frontend", "#welcome-header")
    #     self.assert_element("#tickets div h4")
    #     self.assert_text("t1 100", "#tickets div h4")

    # @patch('qa327.backend.get_user', return_value=test_user)
    # @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    # def test_login_password_failed(self, *_):
    #     """ Login and verify if the tickets are correctly listed."""
    #     # open login page
    #     self.open(base_url + '/login')
    #     # fill wrong email and password
    #     self.type("#email", "test_frontend@test.com")
    #     self.type("#password", "wrong_password")
    #     # click enter button
    #     self.click('input[type="submit"]')
    #     # make sure it shows proper error message
    #     self.assert_element("#message")
    #     self.assert_text("login failed", "#message")
