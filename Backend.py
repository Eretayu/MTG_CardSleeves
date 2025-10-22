from flask import Flask, render_template, request
import sqlite3

######GEEKS FOR GEEKS CONNECTION TESTING CODE######
try:
    # Connect to SQLite Database and create a cursor
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Execute a query to get the SQLite version
    query = 'SELECT sqlite_version();'
    cursor.execute(query)

    # Fetch and print the result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result[0][0]))


except sqlite3.Error as error:
    print('Error occurred -', error)


######GEEKS FOR GEEKS CONNECTION TESTING CODE######

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")
        
@app.route("/intro.html")
def intro():
    return render_template("intro.html")
   

@app.route("/homepage.html")
def homepage():
    return render_template("homepage.html")

def process_data():
    if request.method == "POST":
        username = request.form.get("username")
        if username.find(";") != -1:
            return "Invalid input detected"
        else:
            Query = "SELECT * FROM users WHERE username = '{}';".format(username)
            


        debug = f"Received username: {username}"
        print(debug)
    return "No data received"

        

if __name__ == "__main__":
    app.run(debug=True, port=5001)
"""
cursor.execute("CREATE TABLE users (userID INT UNIQUE, username VARCHAR(50), tblID INT AUTO_INCREMENT PRIMARY KEY NOT NULL);")

sql = f"INSERT INTO users (userID, username) VALUES (%s, %s);"
val = [
    (1, 'testuser')
    (2, 'tobi')
    (3, 'somethingwhocares')
]


cursor.execute(sql,val)


cursor.commit()
cursor.close()
"""


cursor.execute("SHOW TABLES;")

tables = cursor.fetchall()

