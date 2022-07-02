import os
import pickle
from configparser import ConfigParser
from typing import TypedDict


class Storage:
    def __init__(self):
        self.config_obj = ConfigParser()
        self.config_obj.read("settings.ini")
        self.main_settings = self.config_obj["constants"]

        self.file_location = self.main_settings["file_location"]
        self.current_campaign = False

    def get_campaign_data(self):
        try:
            with open(f"{self.file_location}/current_campaign.pickle", "rb") as handle:
                loaded_data = pickle.load(handle)
            return loaded_data
        except FileNotFoundError:
            return False

    def correct_format_check(self, path):
        name, extension = os.path.splitext(path)
        if extension == ".pickle":
            self.update_database_directory(name)
            return True
        else:
            return False

    def update_database_directory(self, path):
        self.file_location = os.path.dirname(path)

        self.config_obj.set("constants", "file_location", os.path.dirname(path))
        with open('settings.ini', 'w') as updates:
            self.config_obj.write(updates)

    class CampaignDTO(TypedDict):
        campaign: str
        heroes: dict

    def store_campaign_dto(self, data):
        with open(f"{self.file_location}/{data.get('campaign')}.pickle", "wb") as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
