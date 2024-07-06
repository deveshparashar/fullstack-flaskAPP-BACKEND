from flask import Flask

app = Flask(__name__) # consturctor __name__ which is the main module

@app.route('/') #decorator
def index():
    return 'Hello world'

# Dynamic Routing 

@app.route('/<name>')
def print_name(name):
    return "Welcome, {}".format(name)

if __name__=='__main__':
    app.run(debug=True)