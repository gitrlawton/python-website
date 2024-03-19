## app.py is the entry point for our website. ##

# Import Flask
from flask import Flask
# Import our blueprint variable named views from views.py.
from views import views

# Intialize our Flask application.
app = Flask(__name__)
# Link/register the blueprint from views.py to our flask app.
app.register_blueprint(views, url_prefix="/")

# Run the application.
if __name__ == '__main__':
    app.run(debug = True)