Requirement 4: /Sell

Test Data:
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test ticket yo',
    quantity=10,
    price=10,
    date='20200901'
)
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
Test case R4.1- Name of ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - positive

Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket_valid_name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_name_message element shows valid and sell_submit message shows successful
•	Open /logout
Test case R4.1- Name of ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - negative

Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket_invalid_name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_name_message element shows invalid and the sell_submit message shows unsuccessful
•	Open /logout
Test case R4.2 - Name of ticket is no longer than 60 characters - positive
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket's LTsixtychname into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_name_message element shows valid and the sell_submit message shows successful
•	Open /logout
Test case R4.2 - Name of ticket is no longer than 60 characters - negative
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket's GTsixtychname into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_name_message element shows invalid and the sell_submit message shows unsuccessful
•	Open /logout
Test case R4.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100. - positive 
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket's name into element #sell_name
•	enter test_ticket_50 into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_quantity_message element shows valid and the sell_submit message shows successful
•	Open /logout
Test case R4.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100. - negative
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket's name into element #sell_name
•	enter test_ticket_130 into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket_price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_quantity_message element shows invalid and the sell_submit message shows unsuccessful
•	Open /logout
Test case R4.4 - Price has to be of range [10,100] - positive
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket_$15 into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_price element shows valid and the sell_submit message shows successful
•	Open /logout
Test case R4.4 - Price has to be of range [10,100] - negative
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s$125 into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_price element shows invalid and the sell_submit message shows unsuccessful
•	Open /logout
 
Test case R4.5 - Date must be given in the format YYYYMMDD (e.g. 20200901) - positive
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket_valid_date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_date element shows valid and the sell_submit message shows successful
•	Open /logout
Test case R4.5 - Date must be given in the format YYYYMMDD (e.g. 20200901) - negative
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open /sell
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s_invalid_date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_date_element message shows invalid and the sell_submit message element shows unsuccessful
•	Open /logout
Test case R4.6 - For any errors, redirect back to / and show an error message - positive
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open/sell
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the the sell_submit message element shows unsuccessful
•	Open / 
•	Validate that the error_message element shows the appropriate error message
•	Open /logout
Test case R4.7 - The added new ticket information will be posted on the user profile page
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #sell
•	Open/sell
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the the sell_submit message element shows successful
•	Open / 
•	Validate that the tickets div h4 element displays the correct ticket information
•	Open /logout
Requirement 5: /Update 
Test case R5.1- Name of ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - positive

Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket_valid_name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_name_message element shows valid and sell_submit message shows successful
•	Open /logout
Test case R4.1- Name of ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - negative

Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket_invalid_name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_name_message element shows invalid and the sell_submit message shows unsuccessful
•	Open /logout
Test case R4.2 - Name of ticket is no longer than 60 characters - positive
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket's LTsixtychname into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_name_message element shows valid and the sell_submit message shows successful
•	Open /logout
Test case R4.2 - Name of ticket is no longer than 60 characters - negative
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket's GTsixtychname into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_name_message element shows invalid and the sell_submit message shows unsuccessful
•	Open /logout
Test case R4.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100. - positive 
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket's name into element #sell_name
•	enter test_ticket_50 into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_quantity_message element shows valid and the sell_submit message shows successful
•	Open /logout
Test case R4.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100. - negative
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket's name into element #sell_name
•	enter test_ticket_130 into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket_price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_quantity_message element shows invalid and the sell_submit message shows unsuccessful
•	Open /logout
Test case R4.4 - Price has to be of range [10,100] - positive
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	Open /sell
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket_$15 into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_price element shows valid and the sell_submit message shows successful
•	Open /logout
Test case R4.4 - Price has to be of range [10,100] - negative
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s$125 into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_price element shows invalid and the sell_submit message shows unsuccessful
•	Open /logout
 
Test case R4.5 - Date must be given in the format YYYYMMDD (e.g. 20200901) - positive
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket_valid_date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_date element shows valid and the sell_submit message shows successful
•	Open /logout
Test case R4.5 - Date must be given in the format YYYYMMDD (e.g. 20200901) - negative
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s_invalid_date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the sell_date_element message shows invalid and the sell_submit message element shows unsuccessful
•	Open /logout
Test case R4.6 - For any errors, redirect back to / and show an error message - positive
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the the sell_submit message element shows unsuccessful
•	Open / 
•	Validate that the error_message element shows the appropriate error message
•	Open /logout
Test case R4.7 - The added new ticket information will be posted on the user profile page
Mocking:
•	Mock backend.get_user to return a test_user instance
•	Mock backend.get_ticket to return a test_ticket instance
Actions:
•	open /logout (to invalidate any logged-in sessions that may exist)
•	open /login
•	enter test_user's email into element #email
•	enter test_user's password into element #password
•	click element input[type="submit"]
•	Open /
•	Click element #ticket_name to select ticket
•	Click element #update_ticket
•	enter test_ticket's name into element #sell_name
•	enter test_ticket's quantity into element #sell_quantity
•	Enter test_ticket’s date into element #sell_date
•	Enter test_ticket’s price into element #sell_price
•	Click element #sell_submit
•	Validate that the the sell_submit message element shows successful
•	Open / 
•	Validate that the element tickets div h4 element displays the correct ticket information
•	Open /logout
Requirement 8 : 

