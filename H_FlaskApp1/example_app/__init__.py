'''
Ben Choat 2024/09/12

create_app() is the application factory function

Here we can define routes, blueprints (a more standardized way to create routes),
    initialize Dash apps, databases, and perform other intialization actions.

Run with following in terminal, where "website" is app name (since __init__ is there):
flask --app website run --debug

Some resources:
- User guid: https://flask.palletsprojects.com/en/3.0.x/#user-s-guide
- intro tutorial: https://flask.palletsprojects.com/en/3.0.x/tutorial/
- setting up application factory: https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/


I'm not going into any database material, but there is some commented
    out code referencing a sqlite database. 
    SQLite comes default with Python. It is serverless which makes it 
    very light weight and easy to use. 
HOWEVER, once we deploy we will want our database to be persistent.
    One option would be manually back-up and reinitate a sqlite databse
    each time we deploy an updated version. 
    So, we will be using PostgreSQL, another very popular database management
    system. We can deploy it to AWS RDS and it will be persistent even
    when we update our app.

I'm also not covering config.py... You can define certain environment 
    variables and other configuration options there. Some of those 
    options we are defining here. In deployment, we should use 
    config.py... for example, placing an encrypted secret key there.

'''

from flask import Flask
import os

# test_config is a config file that can be loaded instead of 
# a config file for development testing
def create_app(test_config=None):
       # create and configure the app. Tells app to look for instance config
    # relative to app location
    # Also looks for sqlite file at in instance folder
    # NOTE: example_app.sqlite, because this is the 'website' module since 
    # contains __init__ within website/
    app = Flask(__name__, instance_relative_config=True, static_folder='assets')

    app.config.from_mapping(
        SECRET_KEY='secret_key', # remove for deployment and use 
        # DATABASE=os.path.join(app.instance_path, 'example_app.sqlite'),
    )

    # app.config.from_pyfile() overrides the default configuration with values taken 
    # from the config.py file if it exists. For example, when 
    # deploying, this can be used to set a real SECRET_KEY.
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists; fails silently if already exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass


    # define some routes and content
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        # return 'Seriously though, how much rain does eastern Oregon get???'
        return '<Div><H1>Seriously though, how much rain does eastern Oregon get???</H1></Div>'
    
    @app.route('/')
    def landing():
        from flask import redirect
        return redirect('/hello')


    return app

# Run with following in terminal, where "website" is app name (since __init__ is there):
# flask --app website run --debug