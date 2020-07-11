from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import User
from application.forms import LoginForm, RegisterForm
from email import generate_confirmation_token, confirm_token, send_email, check_confirmed

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

# connect to other people homepage
@app.route("/connect")
def connect():
    return render_template("connect.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('connect'))

    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username',None)
    return redirect(url_for('home'))

@app.route("/community/")
@app.route("/community/<suburb>")
def community(suburb = None):
    if suburb is None:
        suburb = user.suburb
    community = user.objects.order_by("first_name")
    return render_template("community.html")

@app.route("/confirm/<token>")
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('connect')) 

@app.route("/unconfirmed")
@login_required
def unconfirmed():
    if current_user.confirmed:
        return redirect(url_for('connect'))
    flash('Please confirm your account!', 'warning')
    return render_template('/unconfirmed.html')

@app.route("/register", methods=['POST','GET'])
def register():
    if session.get('username'):
        return redirect(url_for('connect'))

    form = RegisterForm()
    if form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     += 1
        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data
        address     = form.address.data
        suburb      = form.suburb.data
        available   = True
        confirmed   = False

        user = User(
            user_id = user_id, 
            email = email, 
            first_name = first_name, 
            last_name = last_name,
            address = address,
            suburb = suburb,
            available = available,
            confirmed = confirmed,
        )
        user.set_password(password)
        user.save()
        token = generate_confirmation_token(user.email)
        confirm_url = url_for('user.confirm_email', token=token, _external=True)
        html = render_template('user/activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)
        login(user)

        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for("unconfirmed"))

        # flash("You are successfully registered!","success")
    return render_template("register.html", title="Register", form=form, register=True)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
@check_confirmed
def profile():
    return render_template("profile.html")

@app.route('/resend')
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('user.confirm_email', token=token, _external=True)
    html = render_template('user/activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('user.unconfirmed'))

@app.route("/user")
def user():
     users = User.objects.all()
     return render_template("user.html", users=users)