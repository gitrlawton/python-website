## This file contains the routes, or views. ##

# A blueprint allows us to put all of our routes in this file instead
# of the main file (app.py).
from flask import Blueprint
# Import the render_template function to allows us to render an HTML
# page we created in our 'templates' folder.
from flask import render_template
# Importing request to allow us to handle query parameters.
from flask import request
# Allows us to turn our data into json.
from flask import jsonify
# Allows us to redirect.
from flask import redirect, url_for

# Blueprint that takes on the name of our file.
views = Blueprint(__name__, "views")

# Use the blueprint to decorate the route.
@views.route("/")
def home():
    # Normally you'd want to return HTML here to be displayed on the
    # page, not just plain text.
    return "This is the Home page."

@views.route("/home2")
def home2():
    # Render index.html which is in our 'templates' folder.
    # We can pass it variable values to be used dynamically in the HTML file.
    return render_template("index.html", name="Ryan")

@views.route("/profile/<username>")
# Parameter(s) below need to match the dynamic variable(s) in the path above.
# Hence, username is present in both.
def profile(username):
    # Set name to username, that way when you visit localhost/profile/john
    # the page says "Hello john!".
    return render_template("index.html", name=username)

# Creating an alternative profile endpoint that can handle query parameters
# example: /profile?name=john      Note: name is the query parameter and its
# value would be john.
# We will be able to just use the base  '/profile' path now with this method
# and not have to declare any parameters for the function either.
@views.route("/profile")
def profile2():
    # Establishing a dictionary named 'args' to access any query parameters. 
    args = request.args
    # Extracting the value from the key 'name' in the args dictionary and 
    # assigning it to a variable 'name'.
    name = args.get("name")
    # We can use this name within our template like so.
    return render_template("index.html", name=name)
    # Now, if you go to localhost/profile?name=Jeremy, the page will display
    # Hello Jeremy!
    
@views.route("/profile-template")
def profile3():
    return render_template("profile.html")

## All the routes up to this point have been returning html.  Below, we ##
## will return json. ##

@views.route("/json")
def get_json():
    # Whatever data you want to return, place it in a dictionary and pass
    # it to the jsonify function.  Just using dummy data here for now.
    return jsonify({
        "name": "Mark",
        "age": 32,
        "occupation": "student"
    })
    # Now if you go to localhost:5000/json  you'll see the data you just 
    # returned in json form.

# Getting data from a request that is incoming.  Someone is going to send
# some json data to this route.
@views.route("/data")
def get_data():
    # How you access the json data from the request, and assign it to 
    # a variable 'data'.
    data = request.json
    # Turn that extracted data back into json and return it.
    return jsonify(data)

# Redirect to a new page.
@views.route("go-to-home")
def go_to_home():
    # As the argument in url_for(), pass it the blueprint name followed
    # by a period, followed by the name of the route to redirect to.
    # The following will take us to the home route, which should display
    # "This is the Home page."  The path in the url bar will change to the
    # path of the route you are redirected to.  In this case, localhost:5000.
    return redirect(url_for("views.home"))