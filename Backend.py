from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/homepage")
def index():
    return render_template("homepage.html")

@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        username = request.form.get('username')

        print(f"Received Username: {username}")
        


if __name__ == "__main__":
    app.run()(debug=True)