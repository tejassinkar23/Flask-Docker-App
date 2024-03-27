from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__,template_folder='templates')
app.secret_key = 'your_secret_key'

# Dummy user credentials
USER_CREDENTIALS = {
    "username": "admin",
    "password": "admin123"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            flash('Login Successful', 'success')
            # Redirect to your application's operations page
            return redirect(url_for('operations'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/operations')
def operations():
    # Implement your application's operations here
    return "Welcome to the application's operations page"

if __name__ == '__main__':
    # Run Flask app on port 5000
    app.run(host='0.0.0.0',debug=True, port=5000)

