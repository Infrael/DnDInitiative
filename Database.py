from typing import TypedDict
import pickle


class CampaignDTO(TypedDict):
    campaign: str
    heroes: dict


def store_data(data):
    with open(f"{data.get('campaign')}.pickle", "wb") as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def get_data(file_name):
    with open(f"{file_name}.pickle", "rb") as handle:
        loaded_data = pickle.load(handle)
    return loaded_data
