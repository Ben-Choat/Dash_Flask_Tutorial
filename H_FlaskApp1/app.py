'''
BChoat 2024/09/12

This file launches the app from the app factory.

We define example_app (name is arbitrary) as a python
package, so it is importable here.

We define a funcition to create the app in 
    example_app/__init__ (this is the 'app factor')



Generic app layout (we are using) is roughly:

src (e.g., H_FlaskApp1)
- app.py (or however you name it, I think I used application.py for OWRD app)
    This is the file you are currently looking at.
    It calls the app factory to run the app.
- app_home_folder (e.g., example_app)
    - __init__.py (where app factory lives)
    - static (holds resrouces such as .png, .csv, etc. )
        Flask expects 'static', we redefine it to be 'assets'
        because that is what Dash uses.
    - templates
        Holds .html files (so page templates)
    - .py files
        any files where we use python for computation, or whatever else
        These could live in another folder, but I've been keeping them here.
    
    
'''

from example_app import create_app

application = create_app()

if __name__ == '__main__':
    application.run(debug = False)