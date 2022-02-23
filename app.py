from flask import Flask

# Create new flask app instance
app = Flask(__name__)

# create flask root
@app.route('/')
def hello_world():
    return 'Hello world'


