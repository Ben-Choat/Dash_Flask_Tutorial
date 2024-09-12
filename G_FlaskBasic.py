'''
BChoat 2024/09/12

A very basic Flask app example.


Some Notes

- There are multiple ways to design a Flask app/website
--- Most basic is shown here:
    includes app definition, route definition, and app execution

--- One can also split these into multiple files

--- To incorporate Dash into flask we use what they refer to
    as an app factory (we will see in a couple of files)

'''

from flask import Flask

# Create a Flask instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Seriously though, how much rain does eastern Oregon get???.'
    # return '<Div><H1>This is html now!!</H1></Div>'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # debug=True will auto-reload the server on code changes

