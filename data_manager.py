import requests
import os


class DataManager:

    def __init__(self):
        self.editUrl = "https://api.sheety.co/5b357c9d798080d953fd0c6e2a14ca9b/myFlights/sheet1/"
        self.getUrl = "https://api.sheety.co/5b357c9d798080d953fd0c6e2a14ca9b/myFlights/sheet1"
        self.headers = {
            "Authorization": os.environ.get('auth_header')
        }

    def get_rows(self):
        response = requests.get(url=self.getUrl, headers=self.headers)
        response.raise_for_status()
        return response

    def edit_row(self, obj_id, params):
        response = requests.put(url=f"{self.editUrl}{obj_id}", json=params, headers=self.headers)
        response.raise_for_status()
        return response
