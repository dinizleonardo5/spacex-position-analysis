from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import mysql.connector

mydb = mysql.connector.connect(host="mysql-container", user="root", passwd="123", database='db_spacex')
my_cursor = mydb.cursor()

my_cursor.execute("""
SELECT * FROM starklink_last_position
""")

row_list =[]
for row in my_cursor:
    row_list.append(row)

app = Flask(__name__)

@app.route("/")
def main():
    return row_list

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@mysql-container:3306/db_spacex'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9001)