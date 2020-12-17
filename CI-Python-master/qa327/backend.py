from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2, balance):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=balance)

    db.session.add(new_user)
    db.session.commit()
    return None
def add_ticket(name,quantity,price,expiration):
    new_ticket = Ticket(name=name,quantity=quantity,price=price,expirationdate=expiration)
    db.session.add(new_ticket)
    db.session.commit()
    return None

def get_ticket(name):
    ticket = Ticket.query.filter_by(name=name).first()
    return ticket

def remove_ticket(name):
    ticket = get_ticket(name)
    db.session.delete(ticket)
    db.session.commit()
    return None

def update_ticket(name,quantity,price,expiration):
    ticket = get_ticket(name)
    ticket.name = name
    ticket.quantity = quantity
    ticket.price = price
    ticket.expirationdate = expiration
    db.session.commit()
    return None

def update_quantity(name,quantity):
    ticket = get_ticket(name)
    ticket.quantity = ticket.quantity - int(quantity)
    db.session.commit()
    return None
    

def ticket_bought(name):
    ticket = get_ticket(name)
    if ticket.quantity == 1:
        remove_ticket(name)
    else:
        ticket.quantity = ticket.quantity-1
    return None

def get_all_tickets():
    tickets = Ticket.query.all()
    return tickets
    
def get_all_tickets():
    tickets = Ticket.query.all()
    return tickets