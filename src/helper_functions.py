import yaml




class ConfigClass(object):
    """Convert a dictionary to an object with attributes being the keys"""

    def __init__(self, dictionary):
        """Constructor"""
        for key in dictionary:
            setattr(self, key, dictionary[key])


def load_yaml(yaml_file):
    """Function for loading configuration in yaml file and make it an object to return"""
    try:
        with open(yaml_file) as f:
            config_dict = yaml.safe_load(f)
            config = ConfigClass(config_dict)
            print(f'Configuration in {yaml_file} loaded')
            return config
    except FileNotFoundError:
        print(f'ERROR - cannot find config file {yaml_file}')