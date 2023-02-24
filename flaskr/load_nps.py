import helper_functions as uf

import requests
import json
from flatten_json import flatten
from pandas import json_normalize
import pandas as pd

from constants import auth_config_path, data_config_path, data_wd


class NPSdataRetriever:
    """class for retrieve data through NPS API

    """

    def __init__(self, authentication: dict, data_config: object):
        """initialize object with API authentication and data configuration

        :param authentication: dict of api authorization, e.g. {'api_key': 'xxxxxx'}
        :param data_config: data configuration object
        """
        self.auth = authentication
        self.data_config = data_config
        self.api_config = uf.ConfigClass(data_config.API)
        self.filename_config = uf.ConfigClass(data_config.filename)

    def get_activities(self):
        """function for retrieving activities possible in national parks

        :return: dataframe including activity id and name
        """
        url = self.api_config.get_activities_url
        r = requests.get(url, params=self.auth)
        data = pd.DataFrame(json.loads(r.text)['data'])
        print(data.shape)
        print(data.head())
        filepath = data_wd + self.filename_config.activities
        data.to_csv(filepath, index=False)
        print(f"Activity data were retrieved and saved in {filepath}")
        return data

    def get_activity_related_parks(self):
        """function for retrieving national parks related to specific activities

        :return:
        """
        url = self.api_config.get_activity_related_park_url
        r = requests.get(url, params=self.auth)
        raw_data = json.loads(r.text)['data']
        data_list = []
        for activity in raw_data:
            for park in activity['parks']:
                data_dict = {}
                data_dict['id'] = activity['id']
                data_dict['name'] = activity['name']
                data_dict['designation'] = park['designation']
                data_dict['state'] = park['states']
                data_dict['parkCode'] = park['parkCode']
                data_dict['parkName'] = park['fullName']
                data_list.append(data_dict)
        data = pd.DataFrame(data_list)
        print(data.shape)
        print(data.head())
        filepath = data_wd + self.filename_config.activity_related_parks
        data.to_csv(filepath, index=False)
        print(f"Activity data were retrieved and saved in {filepath}")
        return data

    def get_amenity(self):
        pass

    def get_amenity_related_parks(self):
        pass

    def get_campground(self):
        pass

    def get_places(self):
        pass

    def get_thingstodo(self):
        pass


if __name__ == '__main__':
    auth = uf.load_yaml(auth_config_path).NPS
    nps_data_config = uf.ConfigClass(uf.load_yaml(data_config_path).NPS)
    nps_data_retriever = NPSdataRetriever(auth, nps_data_config)
    nps_data_retriever.get_activity_related_parks()
