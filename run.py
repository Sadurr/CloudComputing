from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/mail")
def index():
    msg = Message('Hello', sender='yourId@gmail.com', recipients=['someone1@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/help')
def help():
    return "HELP ME!!!"


@app.route('/contact')
def contact():
    return render_template("contact.html")
    # return "<a href=mailto:filipsadurski3@gmail.com>Send email</a>"
    # return "contact with me filipsadurski3@gmail.com: "


@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    if request.method == 'POST':
        return 'HTTP POST for user %s with password %s' % (username, request.form['password'])
    else:
        return 'HTTP GET for user %s' % (username)


@app.route("/error_denied")
def error_denied():
    abort(401)


@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505


@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return request.form["username"] + "+" + request.form["password"]
    else:
        return render_template("login.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


@app.route('/s/')
def pattern():
    return render_template('index.html', user="Andrzej", email="email@mail.com")


if __name__ == "__main__":
    app.run(debug=True)
