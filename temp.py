import configparser
config = configparser.ConfigParser()

# Add the structure to the file we will create
config.add_section('settings')
config.set('settings', 'file_location', 'C:/')

# Write the new structure to the new file
with open(r"/settings.ini", 'w') as configfile:
    config.write(configfile)
