#! /usr/bin/env python3
# coding: utf-8
import requests

class MediaWikiInfo:
    """
    This class will get information from WikiMedia API thanks to GPS coordinates
    coming from Google Geocoding API.
    """

    def get_story_info(self, latitude, longitude):
        """
        This method requests WikiMedia API to get the wikipedia introduction of
        the location the user is looking for
        """

        story_info = {
            "title": "",
            "intro": "",
            "page_link": "",
            "status" : ""
        }

        payload = {
            "action" : 'query',
            "prop" : "extracts",
            "exintro" : "",
            "explaintext" : "",
            "generator" : "geosearch",
            "ggscoord" : str(latitude) + "|" + str(longitude),
            "ggsradius" : "100",
            "format" : "json"
        }

        try:
            req = requests.get("https://fr.wikipedia.org/w/api.php", params=payload)
            data = req.json()
            if data["query"]["pages"]:
                #necessary_data is generated in order to access to the first page
                #returned by the API thanks to its index because the items are
                #pageids, so not known
                necessary_data = list(data["query"]["pages"])
                story_info["title"] = data["query"]["pages"][necessary_data[0]]["title"]
                story_info["intro"] = data["query"]["pages"][necessary_data[0]]["extract"]
                story_info["page_link"] = "https://fr.wikipedia.org/wiki/" + data["query"]["pages"][necessary_data[0]]["title"].replace(" ", "_")
                story_info["status"] = "FOUND"
            else:
                raise KeyError
        except KeyError:
            story_info["status"] = "NOT_FOUND"
        except:
            story_info["status"] = "REQUEST_PROBLEM"

        return story_info
