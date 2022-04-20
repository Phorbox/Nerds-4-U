from re import A
import sys
import os

import mysql.connector
from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for, session, flash

from sympy import Product


from PY_Files import Create_User, Login_User, CONSTANTS, SQL_Queries, Product_Information


app = Flask(__name__)

app.secret_key = 'super secret key'

# Connect to database

DB = mysql.connector.connect(host=CONSTANTS.HOST, user=CONSTANTS.USER,
                             password=CONSTANTS.PASSWORD, database=CONSTANTS.DATABASE)
## Home Page ##


@app.route('/', methods=['GET', 'POST'])
def homepage():

    if request.method == 'POST':

        ##############################################################################
        #                                                                            #
        #   PRODUCT TABLE.CSV HAS WHITESPACE ON TAG COLUMNS USE "%{name}%" to NEGATE #
        #   SPECIFICALLY, HAS \r added to it                                         #
        ##############################################################################

        search_for = request.form['search_bar']

        #########################################################################
        # splicedString = search_for.split( " " )                               #
        # split string that user is searching for, search for each individually #
        #########################################################################

        result = Product_Information.Get_Product_By_Tag(search_for)

        session["search"] = result

        # Does it have an Art Category?

        array_art = Product_Information.Get_Product_By_Category_If_Valid(result, '%Art%')
        session["array_art"] = array_art
        
        # Does it have an Accessories Category?

        array_acc = Product_Information.Get_Product_By_Category_If_Valid(result, '%Accessories%')
        session["array_acc"] = array_acc

        # Does it have an Comic Category?

        array_com = Product_Information.Get_Product_By_Category_If_Valid(result, '%Comics%')
        session["array_com"] = array_com

        # Does it have an Trading Card Category?

        array_trading = Product_Information.Get_Product_By_Category_If_Valid(result, "%Trading Card%")
        session["array_trading"] = array_trading 

        # Does it have an Toys and Models Category?

        array_toys_and_models = Product_Information.Get_Product_By_Category_If_Valid(result, "%Toys & Models%")
        session["array_toys_and_models"] = array_toys_and_models

        return redirect(url_for('searchpage'))

    ################################################################################################
    # Call function to perform SQL Query on specified categories (returns array containing tuples) #
        #
    art_products = Product_Information.Get_Product_By_Catagory(
        'Art')                                                  #
    comic_products = Product_Information.Get_Product_By_Catagory(
        'Comics')                                             #
    toy_products = Product_Information.Get_Product_By_Catagory(
        'Toys & Models')                                        #

    #####################################################################################
    # Recurse through each tuple, only returning the third data column (the image id's) #
    #####################################################################################
                                                                                        #
                                                                                        #
    art_img_ids = (tuple(map(lambda x: x[2], art_products)))                            #
                                                                                        #
                                                                                        #
    comic_img_ids = (tuple(map(lambda x: x[2], comic_products)))                        #
                                                                                        #
                                                                                        #
                                                                                        #
    toy_img_ids = (tuple(map(lambda x: x[2], toy_products)))                            #
                                                                                        #

    return render_template('homepage.html',
                           art_img_ids=art_img_ids,
                           comic_img_ids=comic_img_ids,
                           toy_img_ids=toy_img_ids,
                           art_products=art_products,
                           comic_products=comic_products,
                           toy_products=toy_products
                           )  # Display's homepage when at root directory of website along with all products ##

## Helper Function ##


@app.route('/upload/<filename>')
def send_image(filename):

    # Display images

    return send_from_directory("Images", filename)


## User Login Page ##


@app.route('/userLogin', methods=['GET', 'POST'])
def login():

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access

        username = request.form['username']
        password = request.form['password']

        cursor = DB.cursor()
        cursor.execute(
            'SELECT * FROM user_information WHERE username = %s AND pass = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in our database
        if account:

            # Redirect to home page
            flash('Login Successful!')
            return redirect(url_for('homepage'))
        else:

            # Account doesnt exist or username/password incorrect

            flash('Login Unsuccessful')

    return render_template('login.html')  # Display login page at url/userLogin


@app.route('/userRegristration', methods=['GET', 'POST'])
def register():
    print("WE ARE HERE")
    if request.method == 'POST':
        # user_id = '#'
        # review_score = '#'
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        street_address = request.form['street_address']
        state = request.form['state']
        phone_number = request.form['phone_number']

        tempflash = Create_User.Create_User(
            username, email, password, first_name, last_name, street_address, state, phone_number)
        flash(tempflash)

    return render_template('register_page.html')


@app.route('/searchpage', methods=['GET', 'POST'])
def searchpage():

    # If session["search"] is empty do not display any boxes

    result = session["search"]
    array_art = session["array_art"]
    array_acc = session["array_acc"]
    array_com = session["array_com"]
    array_trading = session["array_trading"]
    array_toys_and_models = session["array_toys_and_models"]
    return render_template('searchpage.html', result = result
                                            , array_art = array_art
                                            , array_acc = array_acc
                                            , array_com = array_com
                                            , array_trading = array_trading
                                            , array_toys_and_models = array_toys_and_models)


@app.route('/createListing', methods=['GET', 'POST'])
def createListing():

    if request.method == 'POST':

        catagory = request.form['listingCategory']
        print(catagory, flush=True)
        list_of_tags = request.form.getlist('boxes')
        title = request.form['title']
        print(title)
        description = request.form['desc']
        image = request.form['image']
        dollar = request.form['dollar']
        cent = request.form['cent']
        quantity = request.form['quantity']
        Product_Information.Insert_New_Product(list_of_tags, title, description,
                           image, dollar, cent, quantity)
        return redirect(url_for('homepage'))

    return render_template('Create_Listing.html')


app.run(debug=True)
