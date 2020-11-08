327 Assignment 2
SeetGeek

R3

Requirement 3: /

Test Data:

test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    date='20200901'
)

Test case R3.1 - If the user is not logged in, redirect to login page

Mocking:
Mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /
- Validate that test_user does not exit
- Open /login

Test case R3.2 - This page shows a header 'Hi {}’.format(user.name)

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /
- Validate that current page contains #welcome-header element

Test case R3.3 - This page shows user balance

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /
- Validate that #balance shows user balance

Test case R3.4 - This page shows a logout link, pointing to /logout

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /
- Validate that /logout shows successful

Test case R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /
- Validate that #buy_quantity shows successful
- Validate that test_users’s email shows successful
- Validate ticket price shows successful

Test case R3.6 - This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- Open /
- Mock backend.get_user to return a test_user instance Actions
- click element input[type="submit"]
- Validate that #buy_quantity shows successful
- Validate username shows successful
- Validate ticket price shows successful
- Validate expiration date shows successful
- Validate this page shows successful

Test case R3.7 - This page contains a form that a user can buy new tickets. Fields: name, quantity

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /
- Validate this page shows successful

Test case R3.8 - This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /
- Validate this page shows successful



Test case R3.9 - The ticket-selling form can be posted to /sell

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /sell
- Validate if ticket-selling form shows successful

Test Case R3.10 - The ticket-buying form can be posted to /buy

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /buy
- Validate if ticket-buying form shows successful
 -open /logout (clean up)

Test case R3.11 - The ticket-update form can be posted to /update

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /update
- Validate if ticket-update form shows successful
- open /logout (clean up)

R7

Requirement 7: /logout

Test case R7.1 - Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- Open /logout
- Validate user does not have access to restricted pages
- open /logout (clean up)
