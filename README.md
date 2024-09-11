# Dash_Flask_Tutorial
A short and simple tutorial to enable use of Plotly, Dash, and Flask



# Steps to follow 

1. Clone this repository to a desired location
    - git clone https://github.com/Ben-Choat/Dash_Flask_Tutorial


2. Install Python (If you don't already have the desired version)
    - Identify an existing version of python that you want to use.
    - I'm using Python 3.11, so suggest you do the same. But I suspect versions >= 3.9 should be fine.
    - If you do not already have the version of Python you want to use, then you need to install it.
        - Only installers for Python 3.12 are available via Python.org ... so,
        - On Windows, using the Microsoft Store may be the easiest approach but it installs to a generic location deep in your user profile.
        - If you desire your python executable to be in a known location, you can check if https://www.python.org/downloads/release/python-3119/ provides an installer (NOTE: 3119 referes to Python 3.11.9)


3. Create a virtual environment (we will use venv)
    - Make sure you are in the directory where you want to create the virtual environment
        - The folder in which this git repo was cloned is a good option.
    - Ensuring the correct version of python is being pointed to, run:
        - python -m venv .venv
    - If the desired version is not being pointed to, you will either need to add it to the path, or call it directly.
        - You can call it directly by explicitly pointing to the executable. E.g., if my executable is at C:/Python/python.exe I would use
            - C:/Python/python.exe -m venv .venv
    - This creates a virtual environment called '.venv'. You can call your environment anything you want, but .venv is pretty standard practice.


4. Install the packages needed to run this tutorial.
    - Activate your virtual environemnt, e.g.,:
        - ./.venv/Scripts/activate (Windows)
        - source ./.venv/bin/activate (Linux)
    - Install the modules listed in requirements.txt (included with this repo)
        - python -m pip install -r requirements.txt (assumes requirements.txt is in current directory, otherwise you need to specify correct location)


5. 

