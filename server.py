from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hi(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:name>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def srepeat(num, name):
    return name * num

@app.errorhandler(404) # only works for error 404, page not found 404 status explicitly
def page_not_found(e):
    return ('Sorry! No response. Try again.'), 404

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.