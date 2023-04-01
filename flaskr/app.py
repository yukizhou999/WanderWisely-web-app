from flask import Flask, render_template
import pandas as pd

# get Activities and Amenities
activities = pd.read_csv("data/activity_related_parks.csv")
activities = activities["name"].unique()

amenities = pd.read_csv("data/amenity_related_parks.csv")
amenities = amenities["name"].unique()

print(activities)
print("_---------------_")
print(amenities)
app = Flask(__name__)

@app.route('/ActivitiesAndAmenities')
def ActivitiesAndAmenities():
    return render_template('ActivitiesAndAmenities.html')

@app.route('/')
def home():
    return render_template('home.html')
  
if __name__ == "__main__":
  app.run(debug = True)
