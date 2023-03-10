import pandas as pd
from itertools import tee
import googlemaps
from datetime import datetime
from collections import defaultdict
import math


API_key = 'AIzaSyB4MUlPIwoZ8SdwZD-XfxRvyW1c_wm0Sy8'#enter Google Maps API key
gmaps = googlemaps.Client(key=API_key)

df = pd.read_csv('park_related_places.csv',usecols = ['id','place_title','lat','lon'])


place_id_dict=defaultdict()
lat_lon_dict=defaultdict(dict)

for ind,row in df.iterrows():
    if math.isnan(row['lat']) or math.isnan(row['lon']):
        place=gmaps.find_place(row['place_title'], input_type= "textquery")
        place_id=place['candidates'][0]['place_id'] if place['candidates'] !=[] else None
        lat_0=gmaps.place(place_id) if place_id !=None else None
        lat=lat_0['result']['geometry']['location']['lat'] if lat_0 !=None else None
        lon_0=gmaps.place(place_id) if place_id !=None else None
        lon=lon_0['result']['geometry']['location']['lng'] if lon_0 !=None else None
        
        
    else: 
        place=gmaps.reverse_geocode((row['lat'],row['lon']))
        place_id=place[0]['place_id'] if place !=[] else None
        lat=row['lat']
        lon=row['lon']
        
    place_id_dict[row['id']]=place_id
    lat_lon_dict[row['id']]={'lat':lat,'lon':lon}
    
df_place_id=pd.DataFrame(place_id_dict.items(), columns=['id', 'place_id'])
df_lat_lon= pd.DataFrame.from_dict(lat_lon_dict, orient="index").reset_index()

df_final=pd.merge(df_place_id, df_lat_lon, how='inner', left_on = 'id', right_on = 'index')
df_final=df_final.drop(columns=['index'])
df_final.to_csv('calculated_distances.csv', sep=';', index=None)  