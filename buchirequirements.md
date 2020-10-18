Test_registration = register_user(email, name, password, password2);


test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)


R2.1: if user has logged in, redirect user to the user profile page - positive
Mocking:
-	Mock backend.get_user to return a test_user instance
Actions:
-	Open/logout (to invalidate any logged in sessions that may exist)
-	Open /login
-	Enter test_users’s email into element #email
-	Enter test_user’s password into element #password
-	Click element input[type=”submit]
-	Open/
-	Validate that current page contains #welcome-header element


R2.1: if user has logged in, redirect user to the user profile page (otherwise show registration page)
Mocking:
-	Mock backend.get_user to return a test_user instance
Actions:
-	Open/logout (to invalidate any logged in sessions that may exist)
-	Open /login
-	Enter test_users’s email into element #email
-	Enter test_user’s password into element #password
-	Click element input[type=”submit]
-	Open/
-	Validate that current page contains #login-failed element
-   open /register

R2.3: The registration page shows a registration form requesting email, username, password, password2 - positive
Mocking
-	Mock backend.get_user to return a test_user instance
Actions: 
-	If mock backend.get_user returns no existing user
-	Open/register
-	Enter email into element #email
-	Enter username into element #username
-	Enter password into #password
-	Enter same password into #password2
-	Click element input[type=”submit”]
-   validate that #register_message shows successful



R2.3: The registration page shows a registration form requesting email, username, password, password2 - negative
Mocking
-	Mock backend.get_user to return a test_user instance
Actions: 
-	Open /logout (to invalidate any logged-in sessions)
-	Open/register
-	Enter email into element #email
-	Enter username into element #username
-	Enter password into #password
-	Enter same password into #password2
-	Click element input[type=”submit”]
-   validate that #register_message shows unsuccessful

R2.5: Email, password, password2 all have to satisfy the same required as R1: - postive
Mocking:
Mocking:
-	Mock backend.register_user
Actions:
-	Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter email into #email
-   Enter test_username username into #name
-	Enter password into #password
-	Enter password into #password2
-	Click element input[type=”submit]
-	Validate whether element #register_message element shows 'success'

R2.5: Email, password, password2 all have to satisfy the same required as R1: - negative
Mocking:
Mocking:
-	Mock backend.register_user
Actions:
-	Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter email into #email
-   Enter test_username username into #name
-	Enter password into #password
-	Enter password into #password2
-	Click element input[type=”submit]
-	Validate whether element #register_message element shows 'invalid password' 

R2.6 : username has to be non-empty, alphanumeric-only and space allowed only if it’s not the first or last character - positive
Mocking:
-	Mock backend.register_user
Actions:
-   Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter register_user's email into #email
-   Enter register_user's username into #name
-	Enter register_user’s. password into #password
-	Enter register_user’s. password into #password2
-	Validate whether element #name_message element shows valid

R2.6 : username has to be non-empty, alphanumeric-only and space allowed only if it’s not the first or last character - negative
Mocking:
-	Mock backend.register_user
Actions:
-   Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter register_user's email into #email
-   Enter register_user's username into #name
-	Enter register_user’s. password into #password
-	Enter register_user’s. password into #password2
-	Validate whether element #name_message element shows 'invalid username'


R2.7: Username has to be longer than 2 characters and less than 20 - positive
Mocking: 
-	Mock backend.register_user
Actions:
-	Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter register_user's email into #email
-   Enter register_user's username into #name
-	Enter register_user’s. password into #password
-	Enter register_user’s. password into #password2
-	Click element input[type=”submit]
-	Validate whether element #name_message element shows valid

R2.7: Username has to be longer than 2 characters and less than 20 - negative
Mocking: 
-	Mock backend.register_user
Actions:
-	Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter register_user's email into #email
-   Enter register_user's username into #name
-	Enter register_user’s. password into #password
-	Enter register_user’s. password into #password2
-	Click element input[type=”submit]
-	Validate whether element #name_message element shows invalid username

R2.8: For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute) - negative
Mocking: 
-	Mock backend.register_user
Actions:
-	Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter email into #email
-   Enter test_username username into #name
-	Enter password into #password
-	Enter password into #password2
-	Click element input[type=”submit]
-	Validate whether element #register_message element shows 'formatting error'
-   open /login
-   validate whether login_message element shows '{} format is incorrect.'.format(the_corresponding_attribute)



R2.8: For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute) - positive
Mocking: 
-	Mock backend.register_user
Actions:
-	Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter email into #email
-   Enter test_username username into #name
-	Enter password into #password
-	Enter password into #password2
-	Click element input[type=”submit]
-	Validate whether element #register_message element shows 'formatting error'
-   open /login
-   validate whether login_message element shows 'successful registration'

R2.9: if email already exists, show message ‘this email has already been used’ - negative
Mocking:
-	Mock backend.register_user 
-	Mock backend.get_user to return a test_user instance
Actions:
-   open /logout (to invalidate any logged-in sessions that may exist)
-   open /login
-   enter test_user's email into element #email
-   enter test_user's password into element #password
-   click element input[type="submit"]
-	Open /register
-   Enter existing_email email into #email
-   Enter test_username username into #name
-	Enter password into #password
-	Enter password into #password2
-	Click element input[type=”submit]
-	Validate that #email_message element shows 'This email has already been used'


R2.9: if email already exists, show message ‘this email has already been used’ - postive
Mocking:
-	Mock backend.register_user 
-	Mock backend.get_user to return a test_user instance
Actions:
-   open /logout (to invalidate any logged-in sessions that may exist)
-   open /login
-   enter test_user's email into element #email
-   enter test_user's password into element #password
-   click element input[type="submit"]
-	Open /register
-   Enter existing_email email into #email
-   Enter test_username username into #name
-	Enter password into #password
-	Enter password into #password2
-	Click element input[type=”submit]
-	Validate that #email_message element shows 'success'




R2.10: If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page - positive
-	Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter email into #email
-   Enter test_username username into #name
-	Enter password into #password
-	Enter password into #password2
-	Click element input[type=”submit]
-	Validate whether element #register_message element shows successful 
-   Enter 5000 into #balance element in account balance
-   open /login

R2.10: If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page - negative
-	Open /logout (to invalidate any logged-in sessions)
-	Open /register
-   Enter email into #email
-   Enter test_username username into #name
-	Enter password into #password
-	Enter password into #password2
-	Click element input[type=”submit]
-	Validate whether element #register_message element shows unsuccessful 



Test case R6.1- Name of ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - positive

Mocking:
-	Mock backend.get_user to return a test_user instance
-	Mock backend.get_ticket to return a test_ticket instance
Actions:
-	open /logout (to invalidate any logged-in sessions that may exist)
-	open /login
-	enter test_user's email into element #email
-	enter test_user's password into element #password
-	click element input[type="submit"]
-	Open /
-	Click element #sell
-	Open /sell
-	enter test_ticket_valid_name into element #sell_name
-	enter test_ticket's quantity into element #sell_quantity
-	Enter test_ticket’s date into element #sell_date
-	Enter test_ticket’s price into element #sell_price
-	Click element #sell_submit
-	Validate that the sell_name_message element shows valid and sell_submit message shows successful
-	Open /logout


Test case R6.1- Name of ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - negative

Mocking:
-	Mock backend.get_user to return a test_user instance
-	Mock backend.get_ticket to return a test_ticket instance
Actions:
-	open /logout (to invalidate any logged-in sessions that may exist)
-	open /login
-	enter test_user's email into element #email
-	enter test_user's password into element #password
-	click element input[type="submit"]
-	Open /
-   Click element #sell
-   Open /sell
-	enter test_ticket_invalid_name into element #sell_name
-	enter test_ticket's quantity into element #sell_quantity
-	Enter test_ticket’s date into element #sell_date
-	Enter test_ticket’s price into element #sell_price
-	Click element #sell_submit
-	Validate that the sell_name_message element shows invalid and the sell_submit message shows unsuccessful
-	Open /logout


Test case R6.2 - Name of ticket is no longer than 60 characters - positive
Mocking:
-	Mock backend.get_user to return a test_user instance
-	Mock backend.get_ticket to return a test_ticket instance
Actions:
-	open /logout (to invalidate any logged-in sessions that may exist)
-	open /login
-	enter test_user's email into element #email
-	enter test_user's password into element #password
-	click element input[type="submit"]
-	Open /
-	Click element #sell
-	Open /sell
-	enter test_ticket's LTsixtychname into element #sell_name
-	enter test_ticket's quantity into element #sell_quantity
-	Enter test_ticket’s date into element #sell_date
-	Enter test_ticket’s price into element #sell_price
-	Click element #sell_submit
-	Validate that the sell_name_message element shows valid and the sell_submit message shows successful
-	Open /logout


Test case R6.2 - Name of ticket is no longer than 60 characters - negative
Mocking:
-	Mock backend.get_user to return a test_user instance
-	Mock backend.get_ticket to return a test_ticket instance
Actions:
-	open /logout (to invalidate any logged-in sessions that may exist)
-	open /login
-	enter test_user's email into element #email
-	enter test_user's password into element #password
-	click element input[type="submit"]
-	Open /
-	Click element #sell
-	Open /sell
-	enter test_ticket's GTsixtychname into element #sell_name
-	enter test_ticket's quantity into element #sell_quantity
-	Enter test_ticket’s date into element #sell_date
-	Enter test_ticket’s price into element #sell_price
-	Click element #sell_submit
-	Validate that the sell_name_message element shows invalid and the sell_submit message shows unsuccessful
-	Open /logout


Test case R6.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100. - positive 
Mocking:
-	Mock backend.get_user to return a test_user instance
-	Mock backend.get_ticket to return a test_ticket instance
Actions:
-	open /logout (to invalidate any logged-in sessions that may exist)
-	open /login
-	enter test_user's email into element #email
-	enter test_user's password into element #password
-	click element input[type="submit"]
-	Open /
-	Click element #sell
-	Open /sell
-	enter test_ticket's name into element #sell_name
-	enter test_ticket_50 into element #sell_quantity
-	Enter test_ticket’s date into element #sell_date
-	Enter test_ticket’s price into element #sell_price
-	Click element #sell_submit
-	Validate that the sell_quantity_message element shows valid and the sell_submit message shows successful
-	Open /logout


Test case R6.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100. - negative
Mocking:
-	Mock backend.get_user to return a test_user instance
-	Mock backend.get_ticket to return a test_ticket instance
Actions:
-	open /logout (to invalidate any logged-in sessions that may exist)
-	open /login
-	enter test_user's email into element #email
-	enter test_user's password into element #password
-	click element input[type="submit"]
-	Open /
-	Click element #sell
-	Open /sell
-	enter test_ticket's name into element #sell_name
-	enter test_ticket_130 into element #sell_quantity
-	Enter test_ticket’s date into element #sell_date
-	Enter test_ticket_price into element #sell_price
-	Click element #sell_submit
-	Validate that the sell_quantity_message element shows invalid and the sell_submit message shows unsuccessful
-	Open /logout

Test case R6.4: The ticket name exists in the database and the quantity is more than the quantity requested to buy - positive
Mocking:
-   Mock backend.get_user to return a test_user instance
-   Mock backend.get_ticket to return a test_ticket instance
Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)
-   open /login
-   enter test_user's email into element #email
-   enter test_user's password into element #password
-   click element input[type="submit"]
-   open /
-   enter test_ticket's name into element #buy_name
-   enter test_ticket's quantity into element #buy_quantity
-   click element #buy_submit
-   validate that the #buy_message element shows successful
-   open /logout (clean up)

Test case R6.4: The ticket name exists in the database and the quantity is more than the quantity requested to buy - negative
Mocking:
-   Mock backend.get_user to return a test_user instance
-   Mock backend.get_ticket to return a test_ticket instance
Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)
-   open /login
-   enter test_user's email into element #email
-   enter test_user's password into element #password
-   click element input[type="submit"]
-   open /
-   enter test_ticket's name into element #buy_name
-   enter test_ticket's quantity into element #buy_quantity
-   click element #buy_submit
-   validate that the #buy_message element shows 'The ticket does not exist'
-   open /logout (clean up)


R6.5: The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) - positive
Mocking:
-   Mock backend.get_user to return a test_user instance
-   Mock backend.get_ticket to return a test_ticket instance
Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)
-   open /login
-   enter test_user's email into element #email
-   enter test_user's password into element #password
-   click element input[type="submit"]
-   open /
-   enter test_ticket's name into element #buy_name
-   enter test_ticket's quantity into element #buy_quantity
-   click element #buy_submit
-   validate that the #buy_message element shows successful
-   open /logout (clean up)

R6.5: The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) - negative
Mocking:
-   Mock backend.get_user to return a test_user instance
-   Mock backend.get_ticket to return a test_ticket instance
Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)
-   open /login
-   enter test_user's email into element #email
-   enter test_user's password into element #password
-   click element input[type="submit"]
-   open /
-   enter test_ticket's name into element #buy_name
-   enter test_ticket's quantity into element #buy_quantity
-   click element #buy_submit
-   validate that the #buy_message element shows 'balance not sufficient for the ticket price'
-   open /logout (clean up)


R6.6: 	For any errors, redirect back to / and show an error message
Mocking:
-   Mock backend.get_user to return a test_user instance
-   Mock backend.get_ticket to return a test_ticket instance
Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)
-   open /login
-   enter test_user's email into element #email
-   enter test_user's password into element #password
-   click element input[type="submit"]
-   open /
-   enter test_ticket's name into element #buy_name
-   enter test_ticket's quantity into element #buy_quantity
-   click element #buy_submit
-   validate that the #buy_message element shows unsuccessful
-   open /
-   validate that #error_message shows error with ticket
-   open /logout (clean up)

