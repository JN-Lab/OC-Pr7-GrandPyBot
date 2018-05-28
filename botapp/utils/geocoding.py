#! /usr/bin/env python3
# coding: utf-8
from config import Config
import requests

class GeocodingLocation:

    def __init__(self):
        self.api_key = Config.GEOCODING_GOOGLE_API_KEY

    def get_location_info(self, location):
        location = location.replace(" ", "+")

        location_info = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "status" : ""
        }

        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location + "&components=country:FR&key=" + self.api_key

        req = requests.get(url)
        data = req.json()

        try:
            if data["results"][0]["geometry"]["location_type"] != "APPROXIMATE":
                location_info["address"] = data["results"][0]["formatted_address"]
                location_info["latitude"] = data["results"][0]["geometry"]["location"]["lat"]
                location_info["longitude"] = data["results"][0]["geometry"]["location"]["lng"]
                location_info["status"] = "found"
            else:
                raise KeyError
        except KeyError:
            location_info["status"] = "not found"

        return location_info
