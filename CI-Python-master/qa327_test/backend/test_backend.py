import pytest
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from qa327.backend import login_user
from qa327.backend import register_user
from qa327.backend import get_user
from qa327.backend import get_ticket
from qa327.backend import add_ticket

def test_login_user_method():

    user = get_user("correct_email")
    if not user:
        register_user("correct_email", "test_name", "correct_password", "correct_password", 0)
    assert login_user("correct_email", "correct_password") == get_user("correct_email")
    assert login_user("correct_email", "incorrect_password") == None
    assert login_user("unregistered_email", "test_password") == None

def test_get_ticket_method():#maybe test addticket
    ticket = get_ticket("Correct Ticket")
    if not ticket:
        add_ticket("Correct Ticket", "11", "11","20210101")
    assert get_ticket(" no") == None #test for incorrect ticket name

        

