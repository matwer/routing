from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# Create a server file that generates the specified responses for the following url requests
# localhost:5000/ - have it say "Hello World!"
@app.route('/')

def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode

# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')

def dojo():
    return 'Dojo!' # Return the string 'Dojo!' as a response

# Create one url pattern and function that can handle the following examples:
#   localhost:5000/say/flask - have it say "Hi Flask!"
#   localhost:5000/say/michael - have it say "Hi Michael!"
#   localhost:5000/say/john - have it say "Hi John!"

@app.routecopy('/hello/<name>') # for a route '/say/____' anything after '/say/' gets passed as a variable 'name'

def say(name):
    print(name)
    return "Hi " + name + "!"

# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
#   localhost:5000/repeat/35/hello - have it say "hello" 35 times
#   localhost:5000/repeat/80/bye - have it say "bye" 80 times
#   localhost:5000/repeat/99/dogs - have it say "dogs" 99 times

@app.routecopy('/repeat/<ctr>/<string>')

def repeat(ctr, string):
    ctr = int(ctr)
    for x in range(ctr):
        return string

