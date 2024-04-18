from flask import Flask     # from the flask module import the Flask class

app = Flask(__name__)       # Create an instance of the Flask class

@app.get("/about")
@app.get("/")               # Flask decorator that maps view functions to routes
def index():                # view function
    me = {                  # python dictionary
        "first_name": "Rafael",
        "last_name": "GPL",
        "hobbies": "DIY stuff",
        "is_online": True
    }
    return me               # When you return a dict from a view function, it becomes JSON
