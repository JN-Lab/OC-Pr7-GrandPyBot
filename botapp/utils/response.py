#! /usr/bin/env python3
# coding: utf-8
from .message_parse import MessageParser
from .geocoding import GeocodingLocation
from .mediawiki import MediaWikiInfo

class Response:

    def __init__(self):
        self.message_parser = MessageParser()
        self.gps_seeker = GeocodingLocation()
        self.story_seeker = MediaWikiInfo()

    def get_info(self, message):

        infos = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : ""
        }

        location = self.message_parser.identify_location(message)

        if location:
            geo_info = self.gps_seeker.get_location_info(location)
            if geo_info["status"] == "FOUND":
                infos["address"] = geo_info["address"]
                infos["latitude"] = geo_info["latitude"]
                infos["longitude"] = geo_info["longitude"]
                story_info = self.story_seeker.get_story_info(geo_info["latitude"], geo_info["longitude"])
                if story_info["status"] == "FOUND":
                    infos["title"] = story_info["title"]
                    infos["intro"] = story_info["intro"]
                    infos["page_link"] = story_info["page_link"]
                    infos["status"] = "COMPLETE"
                elif story_info["status"] == "NOT_FOUND":
                    infos["status"] = "STORY_MISSING"
                elif story_info["status"] == "REQUEST_PROBLEM":
                    infos["status"] = "WIKIMEDIA_API_PROBLEM"

            elif geo_info["status"] == "NOT_FOUND":
                infos["status"] = "WRONG_LOCATION"
            elif geo_info["status"] == "REQUEST_PROBLEM":
                infos["status"] = "GOOGLE_GEOCODING_API_PROBLEM"

        else:
            infos["status"] = "LOCATION_MISSING"

        print(geo_info)
        return infos
