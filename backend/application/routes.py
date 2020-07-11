from application import app, db, login, register, add_info, search
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import User

from json import dumps
from flask import Flask, request


@app.route("/login", methods=['POST'])
def user_login():
    email = request.form.get('email')
    password = request.form.get('password')
    info = login(email, password)
    return dumps(info)
    

@app.route("/register", methods=['POST'])
def user_register():
    
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    gender = request.form.get('gender')
    birthday = request.form.get('birthday')
    address = request.form.get('address')
    suburb = request.form.get('suburb')
    postcode = request.form.get('postcode')
    info = register(email, password, first_name, last_name, birthday, gender, address, suburb, postcode)

    return dumps(info)
# connect to other people
# show user first name, last name, age, description, profile pic
@app.route("/users", methods=['GET', 'POST'])
def show_users():
    # probs will get token, not id - need to find id
    id = request.args.get('id')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    info = search(first_name, last_name, id)
    
    return dumps(info)

@app.route("/add-info", methods=['GET'])
def add_profile_info():
    id = request.args.get('id')
    encoded_url = request.args.get('photo')
    description = request.args.get('description')
    add_info (description, encoded_url, id)

