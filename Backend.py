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

    # Close the cursor after use
    cursor.close()

except sqlite3.Error as error:
    print('Error occurred -', error)

finally:
    # Ensure the database connection is closed
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')

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

cursor.execute()




cursor.commit()
cursor.close()




query1 = "SELECT * FROM users"
cursor.execute(query1)
records = cursor.fetchall()
for x in records:
    print(x)

