from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/homepage")
def index():
    username = request.form.get('username')     
    user = "tester"
    if username == user:
        return "good job!"
    else:
        return "Invalid User"
    
    
    




        

if __name__ == "__main__":
    app.run(debug=True)