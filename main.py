import configparser
from file_reader import read_file

config = configparser.ConfigParser()
config.read('config.ini')

source_file = config['files']['source']
destination_file = config['files']['destination']

content = read_file(source_file)

with open(destination_file, 'w') as file:
    file.write(content)
