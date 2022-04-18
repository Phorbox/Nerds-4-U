from re import A
import sys
import os
from PY_Files import Create_User,Login_User,CONSTANTS,SQL_Queries


from flask import Flask, jsonify,request, render_template,send_from_directory,redirect,url_for,session, flash

from nerd4U.Product_Information import Get_Product_By_Catagory

app = Flask(__name__)

app.secret_key = 'super secret key'

import mysql.connector
DB = mysql.connector.connect(host = CONSTANTS.HOST, user =  CONSTANTS.USER, password = CONSTANTS.PASSWORD, database = CONSTANTS.DATABASE)

## Home Page ##
@app.route('/', methods=['GET', 'POST'])
def homepage():

    ################################################################################################
    # Call function to perform SQL Query on specified categories (returns array containing tuples) #
                                                                                                   #
    art_products = Get_Product_By_Catagory('Art')                                                  #
    comic_products = Get_Product_By_Catagory('Comics')                                             #
    toy_products = Get_Product_By_Catagory('Toys & Models')                                        #

    #####################################################################################
    # Recurse through each tuple, only returning the third data column (the image id's) #
    #####################################################################################
                                                                                        #
    art_img_ids     = (tuple(map(lambda x: x[2], art_products)))                        #
                                                                                        #
                                                                                        #
    comic_img_ids   = (tuple(map(lambda x: x[2], comic_products)))                      #
                                                                                        #
                                                                                        #
    toy_img_ids     = (tuple(map(lambda x: x[2], toy_products)))                        #
                                                                                        #
    return render_template('homepage.html', 
                            art_img_ids     =art_img_ids, 
                            comic_img_ids   =comic_img_ids,
                            toy_img_ids     =toy_img_ids,
                            art_products    =art_products,
                            comic_products  =comic_products,
                            toy_products    =toy_products
                            ) ## Display's homepage when at root directory of website along with all products ##


## Helper Function ##
@app.route('/upload/<filename>')
def send_image(filename):

    # Display images 

    return send_from_directory("Images",filename)


## User Login Page ##
@app.route('/userLogin', methods=['GET','POST'])
def login():

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access


        username = request.form['username']
        password = request.form['password']

        # Check if account exists using MySQL
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM user_information WHERE username = %s AND pass = %s', (username, password))

        # Fetch one record and return result
        account = cursor.fetchone()

        # If account exists in accounts table in out database
        if account:
            # Redirect to home page
            flash('Login Successful!')
            return redirect(url_for('homepage'))
        else:
            # Account doesnt exist or username/password incorrect
            flash('Login Unsuccessful')
    # Show the login form with message (if any)
    
    return render_template('login.html')
    

@app.route('/userRegristration', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        
        username =          request.form['username']
        email =             request.form['email']
        password =          request.form['password']
        first_name =        request.form['first_name']
        last_name =         request.form['last_name']
        street_address =    request.form['street_address']
        state =             request.form['state']
        phone_number =      request.form['phone_number']
        
        tempflash = Create_User.Create_User(username, email, password, first_name, last_name, street_address, state, phone_number)
        print(tempflash)
        flash(tempflash)

    return render_template('register_page.html')

app.run(debug=True)

