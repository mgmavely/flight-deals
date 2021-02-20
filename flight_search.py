import requests
import os
import datetime as dt



class FlightSearch:

    def __init__(self):
        self.iata_url = "https://tequila-api.kiwi.com/locations/query"
        self.price_url = "https://tequila-api.kiwi.com/v2/search"
        self.headers = {
            "apikey": os.environ.get("tq_apikey")
        }
        self.home = "YTO"

    def iata(self, location):
        params = {
            "term": location
        }
        response = requests.get(url=self.iata_url, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()['locations'][0]['code']

    def price(self, location):
        current_date = dt.datetime.now().strftime("%d/%m/%Y")
        next_six_months = dt.date.today() + dt.timedelta(days=180)
        next_six_months = next_six_months.strftime("%d/%m/%Y")
        params = {
            "fly_from": self.home,
            "fly_to": location,
            "date_from": current_date,
            "date_to": next_six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "CAD",
            "max_stopovers": 0

        }
        try:
            response = requests.get(url=self.price_url, params=params, headers=self.headers)
            data = response.json()['data'][0]
        except IndexError:
            return 'None'

        flight_info = {
            "price": data["price"],
            "origin_city": data["route"][0]["cityFrom"],
            "origin_airport": data["route"][0]["flyFrom"],
            "destination_city": data["route"][0]["cityTo"],
            "destination_airport": data["route"][0]["flyTo"],
            "out_date": data["route"][0]["local_departure"].split("T")[0],
            "return_date": data["route"][1]["local_departure"].split("T")[0]
        }
        return flight_info


