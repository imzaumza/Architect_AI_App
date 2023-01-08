from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

    
if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> 7c23af4bd423e6a54aa93fb5ebf193b5f110885d
