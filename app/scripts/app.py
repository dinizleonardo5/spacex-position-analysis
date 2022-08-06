from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

# Create a Flask Instance
app = Flask(__name__)

# Configure Database Access
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123'
app.config['MYSQL_DATABASE_DB'] = 'db_spacex'
app.config['MYSQL_DATABASE_HOST'] = 'mysql-container'

# Initialize Database
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

# Search Endpoint
@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == "POST":
        form_id = request.form['idform']
        form_date = request.form['dateform']
        cursor.execute(f"""SELECT id, longitude, latitude, creation_date 
                           FROM   starlink_hst
                           WHERE id = '{form_id}'
                           """) #AND    CAST(creation_date AS DATE) = '{form_date}'
        conn.commit()
        db_data = cursor.fetchall()
        return render_template('search.html', data=db_data)
    return render_template('search.html')

# Create a route decorator
@app.route("/")
def main():
    return """<a href='http://localhost:9001/search'>Go to localhost:9001/search</a>"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9001)