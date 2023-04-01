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

# record user's selection
user_selection = {"activities":[], "amenities":[]}


def update_selection(selection, select_type):
    if selection in user_selection[select_type]:
        user_selection[select_type].remove(selection)
    else:
        user_selection[select_type].append(selection)
    

app = Flask(__name__)

@app.route('/ActivitiesAndAmenities')
def ActivitiesAndAmenities():
    return render_template('ActivitiesAndAmenities.html',activities = activities, amenities = amenities)

@app.route('/record_button', methods=['POST'])
def record_button():
    data = request.get_json()
#    if data["type"] == "activity":
#        user_selection["activities"].append(data['input'])
#    else:
#        user_selection["amenities"].append(data["input"])
    update_selection(data["input"], data["type"])

    print(user_selection)

    # Record the button click in the database or perform any other action
    return '', 204


@app.route('/')
def home():
    return render_template('home.html')
  
if __name__ == "__main__":
  app.run(debug = True)
