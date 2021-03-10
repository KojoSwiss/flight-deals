import requests
from pprint import pprint

sheety_get_endpoint = "https://api.sheety.co/030c15a7e6cf42aefb7c29f533ff9b65/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_get_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_get_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)