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
        if len(form_date) == 10 and form_date.count('-') == 2:
            cursor.execute(f"""
                            SELECT   id, longitude, latitude, creation_date, 
                                     ABS(DATEDIFF(creation_date, CAST('{form_date}' as DATE))) as diff_days_search_date_x_found_date
                            FROM     starlink_hst
                            WHERE    LTRIM(RTRIM(id)) = '{form_id}'
                            ORDER BY 5,4 DESC
                            LIMIT    1
                            """)
            conn.commit()
            db_data = cursor.fetchall()
            if db_data:
                return render_template('search.html', data=db_data, searched_date=form_date, idform=form_id)
            else:
                no_data = 'No data found.'
                return render_template('search.html', no_data=no_data, searched_date=form_date, idform=form_id)
        else:
            error_msg = 'Wrong date format. Make sure your date is in the right format (yyyy-mm-dd)'
            return render_template('search.html', error_msg=error_msg, searched_date=form_date, idform=form_id)
    return render_template('search.html')

# Create a route decorator
@app.route("/")
def main():
    return """<a href='http://localhost:9001/search'>Go to localhost:9001/search</a>"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9001)