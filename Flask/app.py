from flask import Flask, render_template

app = Flask(__name__) # It creates the instace of the Flask class, WSGI app

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug= True)