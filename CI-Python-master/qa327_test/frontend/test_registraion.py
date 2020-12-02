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
    email='jivanji_adnan@test.com',
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
    def test_logout(self, *_):
        """
        This is a front end unit test to login to home page
        and verify if the logout link is displayed correctly.
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

        # test for logout link
        self.assert_element("#welcome-header")
        self.assert_element("#logout")
        element = self.find_element("#logout")
        assert element.get_attribute("href") == base_url + "/logout"

        # test that logout redirects to '/'
        #URL = self.get_current_url();
        #self.assert_equal(URL, base_url + '/');

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login(self, *_):
        """
        R3.1 This will test the login page and test if the user gets redirected to login page if not logged in
        """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#title")
        #self.assert_text("Log in", "#title")

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
    def test_sell_form(self, *_):
        """
        This is a front end unit test to login to home page
        and verify if the sell form is displayed correctly.
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
        # test for sell form elements
        # enter name, quantity, price, expiration
        # click submit
        # verify that ??
        self.assert_element("#tname")
        self.type("#tname", "ticket_name")
        self.assert_element("#tquantity")
        self.type("#tquantity", "1")
        self.assert_element("#tprice")
        self.type("#tprice", "50.00")
        self.assert_element("#texpiration")
        self.type("#texpiration", "02/03/21")
        self.click("#sell-btn-submit")
        self.assert_element("#welcome-header")
        
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_all_tickets(self, *_):
        """
        R3.5 check to see if tickets displays
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
        self.assert_text("Hi test_frontend", "#welcome-header")
        self.assert_element("#tickets")
        self.assert_text("Here are all available tickets")
     

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_form(self, *_):
        """
        This is a front end unit test to login to home page
        and verify if the update form is displayed correctly.
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
        # test for update form elements
        # enter name, quantity, price, expiration
        # click submit
        # verify that ??
        self.assert_element("#uname")
        self.type("#uname", "ticket_name")
        self.assert_element("#uquantity")
        self.type("#uquantity", "3")
        self.assert_element("#uprice")
        self.type("#uprice", "30.00")
        self.assert_element("#uexpiration")
        self.type("#uexpiration", "03/04/22")
        self.click("#update-btn-submit")
        self.assert_element("#welcome-header")

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buy_form(self, *_):
        """
        R3.7 This will test if buy form is displaying
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
        self.assert_element("#name")
        self.type("#name", "test_name")
        self.assert_element("#quantity")
        self.type("#quantity", "1")
        self.click("#buy-btn-submit")
        #self.assert_element("#welcome-header")

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

class RegistrationTest(BaseCase):
           
    #This function checks for an error message when password1 and password2 don't match
    def test_passwords_dont_match(self, *_):
        #open register page
        self.open(base_url + '/register')
        #fill email and passwords that don't match
        self.type("#email", "test_frontend@testing.com")
        self.type("#name", "test_frontend")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualAssura327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows correct error message
        self.assert_element("#message")
        self.assert_text("password1 and password2 don't match", "#message")
    
    #This function checks whether the registration was successful when both passwords match
    def test_passwords_match(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email and passwords that match
        self.type("#email", "edinsoncavanie3@testing.com")
        self.type("#name", "test frontend")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and checks if no error message is displayed
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    #This function checks whether the registration fails when username field is empty
    def test_empty_username(self, *_):
        #open register page
        self.open(base_url + '/register')
        #leave username field as empty
        self.type("#email", "test_frooonten@testing.com")
        self.type("#name", "")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')
        #Since the field username is required, page wont be redirected to login.
        #By checking if regsitration form is still being displayed through one of its elements,
        #we have verified that the form submission failed.
        self.assert_element('#name')

    #This function checks whether the registration fails when password field is empty
    def test_empty_password(self, *_):
        #open register page
        self.open(base_url + '/register')
        #leave password field as empty
        self.type("#email", "test_frrrronten@testing.com")
        self.type("#name", "AmaarJivanji")
        self.type("#password", "")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')
        #Since the field username is required, page wont be redirected to login.
        #By checking if regsitration form is still being displayed through one of its elements,
        #we have verified that the form submission failed.
        self.assert_element('#name')
    
    #This function checks whether the registration fails when email field is empty
    def test_empty_email(self, *_):
        #open register page
        self.open(base_url + '/register')
        #leave email field as empty
        self.type("#email", "")
        self.type("#name", "AmaarJivanji")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')
        #Since the field username is required, page wont be redirected to login.
        #By checking if regsitration form is still being displayed through one of its elements,
        #we have verified that the form submission failed.
        self.assert_element('#name')
    
    #This function checks whether the registration fails when username is lte 2 characters
    def test_short_username(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email, passwords and username shorter than 3 characters
        self.type("#email", "test_frrronten@testing.com")
        self.type("#name", "ab")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows correct error message
        self.assert_element("#message")
        self.assert_text("username too short or too long", "#message")
    
    #This function checks whether the registration fails when username gte 20 characters
    def test_long_username(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email, passwords and username greater than 19 characters
        self.type("#email", "test_frontend@testing.com")
        self.type("#name", "amaarmoizmohammedalijivanji")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows correct error message
        self.assert_element("#message")
        self.assert_text("username too short or too long", "#message")
    
    #This function checks whether registration fails when username has space at beginning
    def test_space_beginning(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email, passwords and username with space at beginning
        self.type("#email", "test_frontend@testing.com")
        self.type("#name", " paulPogba")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows error message
        self.assert_element("#message")
        self.assert_text("space at start/end", "#message")
    
    #This function checks whether registration fails when username has space at the end
    def test_space_end(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email, passwords and username with space at end
        self.type("#email", "test_frontend@testing.com")
        self.type("#name", "paulPogba ")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows error message
        self.assert_element("#message")
        self.assert_text("space at start/end", "#message")
    
    #This function checks whether registration fails when password doesn't have any special characters
    def test_password_without_specialcharacters(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email, username and password with no special characters
        self.type("#email", "test_frontend@testing.com")
        self.type("#name", "AmaarJivanji")
        self.type("#password", "QualityAssurance327")
        self.type("#password2", "QualityAssurance327")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows error message
        self.assert_element("#message")
        self.assert_text("password doesn't meet required complexity", "#message")
    
    #This function checks whether registration fails when password has no uppercase letter
    def test_password_without_uppercase(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email, username and password with no uppercase letters
        self.type("#email", "test_frontend@testing.com")
        self.type("#name", "AmaarJivanji")
        self.type("#password", "qualityassurance327$")
        self.type("#password2", "qualityassurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows error message
        self.assert_element("#message")
        self.assert_text("password doesn't meet required complexity", "#message")

    #This function checks whether registration fails when password has no lowercase letter
    def test_password_without_lowercase(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email, username and password with no lowercase letters
        self.type("#email", "test_frontend@testing.com")
        self.type("#name", "AmaarJivanji")
        self.type("#password", "QUALITYASSURANCE327$")
        self.type("#password2", "QUALITYASSURANCE327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows error message
        self.assert_element("#message")
        self.assert_text("password doesn't meet required complexity", "#message")

    #This functions checks whether registration fails when password is lt 6 characters
    def test_password_short(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email, username and password with 5 characters
        self.type("#email", "test_frontend@testing.com")
        self.type("#name", "AmaarJivanjishort")
        self.type("#password", "Qua$3")
        self.type("#password2", "Qua$3")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows error message
        self.assert_element("#message")
        self.assert_text("password doesn't meet required complexity", "#message")
    
    #This function checks whether registration succeeds when passwords inputted are valid
    def test_valid_password(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill email, passwords and username - all valid
        self.type("#email", "zebradonkey3@testing.com")
        self.type("#name", "AmaarJivanji")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and checks if no error message is displayed
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
    
    #This function checks whether registration fails when email submitted is already taken
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_email_already_used(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill passwords, username and email that has already been used
        self.type("#email", "jivanji_adnan@test.com")
        self.type("#name", "AmaariiiJivanji")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows error message
        self.assert_element("#message")
        self.assert_text("this email has already been used", "#message")
    
    #This function checks whether the email follows the addr-spec defined in RFC 5322   
    def test_valid_email(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill invalid email
        self.type("#email", "jicom")
        self.type("#name", "AmaariiiJivanji")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows error message
        self.assert_element("#message")
        self.assert_text("email not valid", "#message")
    
    #This function checks whether registrations fails when username is not alphanumeric
    def test_username_notalnum(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill invalid email
        self.type("#email", "amaarsmolsky@hotmail.com")
        self.type("#name", "Ama%4rJIVANJI")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened and check if message shows error message
        self.assert_element("#message")
        self.assert_text("name not alphanumeric", "#message")
    #This function confirms that the user balance is set to 5000 when new user is registered
    def test_registration_and_userbalance(self, *_):
         #open register page
        self.open(base_url + '/register')
        #fill invalid email
        self.type("#email", "LiaAmaar1239@gmail.com")
        self.type("#name", "Muhammad Ahmed")
        self.type("#password", "QualityAssurance327$")
        self.type("#password2", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #login page is opened 
        #fill email and password
        self.type("#email", "LiaAmaar1239@gmail.com")
        self.type("#password", "QualityAssurance327$")
        #click enter button
        self.click('input[type="submit"]')

        #user profile page is opened
        #verify that user balance is set to 5000
        self.assert_element("#ubalance")
        self.assert_text(5000, "#ubalance")
      
