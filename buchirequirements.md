Test_registration = register_user(email, name, password, password2);


test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)


R2.1: if user has logged in, redirect user to the user profile page
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

R2.2 & 3:  otherwise, show the user registration page. The registration page shows a registration form requesting email, username, password, password2
Mocking
-	Mock backend.get_user to return a test_user instance
Actions: 
-	If mock backend.get_user returns no existing user
-	Open/register
-	Validate that current page has element email, username, password and password 2


-	Enter email into element #email
-	Enter username into element #username
-	Enter password into #password
-	Enter same password into #password2
-	Click element input[type=”submit”]


****R2.4: the registration form can be submitted as a POST request to the current URL (/request)
Mocking
-	Test self.register()
-	Validate that it is POST request

R2.5: Email, password, password2 all have to satisfy the same required as R1:
Mocking:
-	Mock backend.register_user
Actions:
-	Open /register
-	Validate that element email is not empty and can only be in the form local-part, the symbol @ followed by the domain name. in which the local part is non case sensitive
-	Validate that password is not empty and must meet minimum length 6, at least one upper case, at least one lower case and at least one special character
-	Validate that password 2 is equal to password one

R2.6 : username has to be non-empty, alphanumeric-only and space allowed only if it’s not the first or last character
Mocking:
-	Mock backend.register_user
Actions:
-	Open /register
-	Make a check on element username and verify if the username is empty or not
-	Validate whether username contains only numbers and letters from the alphabet
-	Make sure space is only allowed if it is not the first or last character

R2.7: Username has to be longer than 2 characters and less than 20
Mocking: 
-	Mock backend.register_user
Actions:
-	Open /register
-	Validate whether element username is greater than 2 but less than 20

R2.8: 


R2.9: if email already exists, show message ‘this email has already been used’
Mocking:
-	Mock backend.register_user 
-	Mock backend.get_user to return a test_user instance
Actions:
-	Open /register
-	Enter new users email into get_user element email to check if it returns anything, if it does not return anything then continue
-	If get_user returns a user, then email already exists
-	Validate that it shows ‘this email has already been used’

