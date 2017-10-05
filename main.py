from flask import Flask, request, redirect, render_template
import cgi 
import os 
import jinja2

app = Flask (__name__)
app.config['DEBUG'] = True

@app.route('/validate-login')
def display_login_form():
    return render_template('login_form.html')

@app.route('/validate-login', methods=['POST'])
def validate_login():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    #username character check
    if len(username) < 3:
        username = ''
        username_error = 'Username must be more than three characters.'
    elif len(username) > 20: 
        username = ''
        username_error = 'Username must be less than twenty characters.'
    else: 
        username = username
    
    #password character check
    if 20 < len(password) < 3:
        password = ''
        password_error = 'Password must be betweeen three and twenty characters.'

    #password match check 
    if password != verify_password:
        password = ''
        verify_password = ''
        verify_password_error = 'Password do not match.'
    
    #email validation 
    if len(email) > 0:
        if not (email.endswith('@') or email.startswith('@') or email.endswith('.')
        or email.startswith('.')) and email.count('@') == 1 and email.count('.') == 1:
            email = email
        else:
            email = ''
            email_error = 'Email must contain @/. but not begin or end with those characters.'
    else: 
        email = ''
    
    #empty fields
    if username == '':
        username_error = 'Username must be between three and twenty characters.'
    if password == '':
        password_error = 'Password must be between three and twenty characters.'
    if verify_password == '':
        verify_password_error = 'Passwords do not match.'
    
    #if conditions are met, redirects to confirmation page
    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template('confirmation.html', username = username)
    
    #if conditions are met, returns to signup-form
    else:
        return render_template('login_form.html', username_error=username_error,
            password_error=password_error, verify_password_error=verify_password_error,
            email_error=email_error,
            username=username, 
            password=password,
            verify_password=verify_password,
            email=email)

app.run()
