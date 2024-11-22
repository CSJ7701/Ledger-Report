import configparser

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config.file)
    return config
