#! /usr/bin/env python3
# coding: utf-8
from collections import OrderedDict
import requests

class MediaWikiInfo:

    def get_story_info(self, latitude, longitude):
        story_info = {
            "title": "",
            "intro": "",
            "page_link": "",
            "status" : ""
        }

        url = "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&generator=geosearch&ggscoord=48.8388508|2.2740328&ggsradius=100&format=json"

        try:
            req = requests.get(url)
            data = req.json()
        except:
            story_info["status"] = "REQUEST_PROBLEM"

        try:
            if data["query"]["pages"]:
                necessary_data = list(data["query"]["pages"])
                story_info["title"] = data["query"]["pages"][necessary_data[0]]["title"]
                story_info["intro"] = data["query"]["pages"][necessary_data[0]]["extract"]
                story_info["page_link"] = "https://fr.wikipedia.org/wiki/" + data["query"]["pages"][necessary_data[0]]["title"].replace(" ", "_")
                story_info["status"] = "found"
            else:
                raise KeyError
        except KeyError:
            story_info["status"] = "not found"

        print(necessary_data)
        print(story_info)
        return story_info
