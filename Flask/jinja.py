from flask import Flask, render_template, request

app = Flask(__name__) # It creates the instace of the Flask class, WSGI app

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/index", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/aboutus", methods = ["GET"])
def aboutus():
    return render_template("aboutus.html")

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

@app.route('/successif/<int:score>')
def success(score):
    return render_template('result.html', results = score)
if __name__ == "__main__":
    app.run(debug= True)