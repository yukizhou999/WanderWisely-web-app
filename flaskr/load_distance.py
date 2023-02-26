import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBHD-lOFZgRIJiSSyGzA51S5jFZ6b386NU')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via walking
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="walking",
                                     departure_time=now)
# Request distance via walking
distance_result = gmaps.distance_matrix("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="walking",
                                     departure_time=now)

# find place
find = gmaps.find_place("Kyoto", input_type= "textquery")

# place
# multiple photos
place = gmaps.place(place_id = "ChIJ8cM8zdaoAWARPR27azYdlsA")

# Places
places = gmaps.places(query="kyoto")

# elevation

elevation = gmaps.elevation((37.4220699,-122.084958))


# download photos
local_filename = "test2.jpg"
photo_reference = 'AfLeUgN69bKlZ8SMSL9fS9I8ZZovC3JhxzpTQLDNmWOyTterrav8uRmYhM5BmhqF18jY2AhjBLDH8o5p5k3-HOhaZkF-TaSEIA4S4YI_gteYpjBho6Zyb1azazdSo487r6zutXR3GbVlAVlDwGuPKJhPj9lG84b7wru6WNr-IFSvcdThPhNR'
f = open(local_filename, 'wb')
for chunk in gmaps.places_photo(photo_reference, max_width=5000):
    if chunk:
        f.write(chunk)
f.close()


# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'],
                                                    regionCode='US',
                                                    locality='Mountain View',
                                                    enableUspsCass=True)