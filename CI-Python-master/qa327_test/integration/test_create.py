import pytest
import qa327.backend as bn
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


# integration testing: the test case interacts with the 
# browser, and test the whole system (frontend+backend).

# Moch a sample user
test_user = User(
    email='liamason@gmail.com',
    name='test_frontend',
    password=generate_password_hash('KingstonOntario2$')
)

@pytest.mark.usefixtures('server')
class Registered(BaseCase):

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "liamason@gmail.com")
        self.type("#name", "Lia Mason")
        self.type("#password", "KingstonOntario2$")
        self.type("#password2", "KingstonOntario2$")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "liamason@gmail.com")
        self.type("#password", "KingstonOntario2$")
        self.click('input[type="submit"]')

    def create_tickets(self):
        """Adds a new ticket through sell form. """
        self.open(base_url)
        self.type("#tname", "Mombasa")
        self.type("#tquantity", "20")
        self.type("#tprice", "15")
        self.type("#texpiration", "20210301")
        self.click("#sell-btn-submit")
    '''
    def create_tickets_2(self):
        """Adds a new ticket through sell form. """
        self.open(base_url)
        self.type("#tname", "Superman")
        self.type("#tquantity", "20")
        self.type("#tprice", "15")
        self.type("#texpiration", "20210711")
        self.click("#sell-btn-submit")
    '''
    def buy_tickets(self):
        """Purchases a ticket through buy form. """
        self.open(base_url)
        self.type("#buyname", "Mombasa")
        self.type("#buyquantity", "1")
        self.click("#t-submit")

    def update_ticket(self):
        self.open(base_url)
        self.type("#uname", "Mombasa")
        self.type("#uquantity", "20")
        self.type("#uprice", "15" )
        self.type("#uexpiration", "20210301")
        self.click("#update-btn-submit")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_register_login_create_ticket(self, *_):
        """ This test checks the implemented login/logout feature """
        #self.register()
        self.login()
        self.create_tickets()
        self.open(base_url)
        #should open base url
        self.assert_element("#welcome-header")
        #self.assert_text("Welcome test_frontend", "#welcome-header")
        self.assert_element("#tickets div h4")
        self.assert_text("Title: Mombasa, Price: 15, Quantity: 20, Expiration Date: 20210301")
        bn.remove_ticket("Mombasa")
    '''
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_register_login_buy_ticket(self, *_):
        """ This test checks the implemented login/logout feature """
        #self.register()
        self.login()
        self.update_ticket()
        self.buy_tickets()
        self.open(base_url)
        #should open base url
        self.assert_element("#welcome-header")
        #self.assert_text("Welcome test_frontend", "#welcome-header")
        self.assert_element("#tickets div h4")
        self.assert_text("Title: Mombasa, Price: 15, Quantity: 19, Expiration Date: 20210301")
    '''
