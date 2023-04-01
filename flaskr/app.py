from flask import Flask, render_template, request
import pandas as pd
from database import conn_to_db, sql_query

# build database connection

conn, engine = conn_to_db()


# get Activities and Amenities
activities = sql_query("select * from wanderwisely.activity_related_parks", conn)
activities = list(activities["name"].unique())
amenities = sql_query("select * from wanderwisely.amenity_related_parks", conn)
amenities = amenities["name"].unique()

app = Flask(__name__)

@app.route('/ActivitiesAndAmenities')
def ActivitiesAndAmenities():
    return render_template('ActivitiesAndAmenities.html',activities = activities, amenities = amenities)

@app.route('/record_button', methods=['POST'])
def record_button():
    data = request.get_json()
    activity = data['activity']
    print(activity)
    # Record the button click in the database or perform any other action
    return '', 204

@app.route('/submit_amenities', methods=['POST'])
def submit_amenities():
    selected_amenities = request.form.getlist('amenities[]')
    # Do something with the selected amenities, such as storing them in a database
    print(selected_amenities)
    return 'Selected amenities: ' + ', '.join(selected_amenities)


@app.route('/')
def home():
    return render_template('home.html')
  
if __name__ == "__main__":
  app.run(debug = True)
