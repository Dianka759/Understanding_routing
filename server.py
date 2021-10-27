from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>') 
def hi(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:name>') 
def repeat(num, name):
    return f"{name} * {num} = {name * num}"

@app.errorhandler(404) # only works for error 404, page not found 404 status explicitly
def page_not_found(e):
    return ('Sorry! No response. Try again.'), 404

if __name__=="__main__":
    app.run(debug=True)