import configparser
config = configparser.ConfigParser()
config.read('examples.ini')
print(config.sections())
print(config["database"]["User"])
print(config["database"]["Compression"])
#dict of dict.