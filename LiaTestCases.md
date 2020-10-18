R1

R1: /login

Test Data:

test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

[GET]

R1.1 - If the user hasn't logged in, show the login page

•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
• validate that the page source contains the text 'Log In'

R1.2 - The login page has a message that by default says 'please login'

•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	validate that current page contains #message element
•	validate that the #message element has the text 'please login'

R1.3 - If the user has logged in, redirect to the user profile page

Mocking:

•	Mock backend.get_user to return a test_user instance

Actions:

•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	open /login again
•	validate that current page contains #welcome-header element

R1.4 - The login page provides a login form which requests two fields: email and passwords

•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
• validate that current page contains #email element
• validate that current page contains #password element

[POST]

R1.5 - The login form can be submitted as a POST request to the current URL (/login)

R1.6 - Email and password both cannot be empty

R1.7 - Email has to follow adr-spec defined in RFC 5322

R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character

R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect'.

R1.10 - If email/password are correct, redirect to /

R1.11 - Otherwise, redirect to /login and show message 'email/password combination incorrect'

R6: /buy

[POST]

R6.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

R6.2 - The name of the ticket is no longer than 60 characters

R6.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100.
