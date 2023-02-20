import helper_functions as uf

import requests
import json

from constants import auth_config_path, data_config_path

auth_config = uf.load_yaml(auth_config_path)
data_config = uf.load_yaml(data_config_path)

# retrieve activities possible in parks
url = data_config.NPS['get_activities_url']
r = requests.get(url, params=auth_config.NPS)
print(r.url)
print(r.json())