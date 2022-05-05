from flask import Flask, render_template
app = Flask(__name__)


# render_templates use with "return"
@app.route("/")
def hello_world():
    return render_template('index.html')
    return "<p>Hello, World!</p> second page is Products"

@app.route("/products")
def products():
    return "<p>This is Second Page</p>"

if __name__== "__main__":
    app.run(debug=True, port=8000)