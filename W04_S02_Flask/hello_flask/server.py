from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!!"

@app.route('/hello')
def hello():
    return "<h1>Hello</h1>"

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello 😃 " + name

# @app.route('/hello/<name>/<times>')
# def many_hello(name,times):

#     return f"Hello 😃 {name} " * int(times)

@app.route('/hello/<name>/<int:times>')
def many_hello(name,times):
    return f"Hello 😃 {name} " * times

@app.route('/hello/<name>/<times>')
def many_hello_2(name,times):
    return f"Hello 😃 {name} "+ times

@app.route('/greet/<name>')
def greet(name):
    return render_template("index.html", username=name)

if __name__ == '__main__':
    app.run(debug=True)