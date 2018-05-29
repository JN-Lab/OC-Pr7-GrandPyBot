#! /usr/bin/env python3
# coding: utf-8
from config import Config
import requests

class GeocodingLocation:
    """
    This class will get gps coordinates from Google Geocoding API according
    the location asked by the user in his message.
    """

    def __init__(self):
        self.api_key = Config.GEOCODING_GOOGLE_API_KEY

    def get_location_info(self, location):
        """
        The methods requests Google Geocoding API, gets only the necessary informations
        and sends back them into a dictionnary
        """

        location = location.replace(" ", "+")

        location_info = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "status" : ""
        }

        payload = {
            "address" : location,
            "components" : "country:FR",
            "key" : self.api_key
        }

        try:
            req = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params=payload)
            data = req.json()
            if data["results"][0]["geometry"]["location_type"] != "APPROXIMATE":
                location_info["address"] = data["results"][0]["formatted_address"]
                location_info["latitude"] = data["results"][0]["geometry"]["location"]["lat"]
                location_info["longitude"] = data["results"][0]["geometry"]["location"]["lng"]
                location_info["status"] = "found"
            else:
                raise KeyError
        except KeyError:
            location_info["status"] = "not_found"
        except:
            location_info["status"] = "REQUEST_PROBLEM"

        return location_info
