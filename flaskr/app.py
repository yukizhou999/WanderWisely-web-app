from flask import Flask, render_template, request
import pandas as pd
import helper_functions as uf


# build database connection

conn, engine = uf.conn_to_db()

# get Activities and Amenities
activities = uf.import_data("select * from wanderwisely.activity_related_parks", conn)
activities = activities["name"].unique()
amenities = uf.import_data("select * from wanderwisely.amenity_related_parks", conn)
amenities = amenities["name"].unique()
# load data to map parkCode to parkName
parks_df = uf.import_data(f"select * from wanderwisely.activity_related_parks", conn)
# record user's selection
user_selection = {"activities": [], "amenities": [], "pois": []}


def update_selection(selection, select_type):
    if selection in user_selection[select_type]:
        user_selection[select_type].remove(selection)
    else:
        user_selection[select_type].append(selection)


app = Flask(__name__)


@app.route('/ActivitiesAndAmenities')
def ActivitiesAndAmenities():
    return render_template('ActivitiesAndAmenities.html', activities=activities, amenities=amenities)


@app.route('/record_button', methods=['POST'])
def record_button():
    data = request.get_json()
    update_selection(data["input"], data["type"])
    # Record the button click in the database or perform any other action

    return '', 204


@app.route('/parks')
def parks():
    top_three_parks = algo(user_selection)
    return render_template('parks.html',parks = top_three_parks)


def generate_places(parkName, activities):
    parkCode = parks_df[parks_df['parkName'] == parkName]['parkCode'][0]
    query = f"select thing_title from wanderwisely.things_to_do_places where parkCode = '{parkCode}' and activity_name in ('{activities}')"
    places_df = uf.import_data(query, conn)
    filtered_places = places_df['thing_title'].to_list()
    return parkName, filtered_places


@app.route('/poi')
def poi():
    parkName = user_selection['parkName']
    activities = user_selection['activities']
    # parkName, places = generate_places(parkName, activities)
    parkName, places = generate_places('acad', ['Biking', 'Hiking'])
    return render_template('poi.html', parkName=parkName, places=places)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
<<<<<<< Updated upstream
    app.run(debug=True)





=======

    app.run(debug=True)
>>>>>>> Stashed changes
