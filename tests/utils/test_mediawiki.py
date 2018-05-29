#! /usr/bin/env python3
# coding: utf-8
from botapp.utils.mediawiki import MediaWikiInfo
import requests
from io import BytesIO
import json

class TestMediaWikiInfo:

    def test_request_info_success(self, monkeypatch):

        # JSON response from the Media Wiki API
        req_result = {
            "batchcomplete": "",
            "warnings": {
                "query": {
                    "*": "Unrecognized value for parameter \"prop\": url."
                }
            },
            "query": {
                "pages": {
                    "854335": {
                        "pageid": 854335,
                        "ns": 0,
                        "title": "H\u00f4pital europ\u00e9en Georges-Pompidou",
                        "index": 0,
                        "extract": "L'h\u00f4pital europ\u00e9en Georges-Pompidou (HEGP) est un h\u00f4pital de l'Assistance publique - h\u00f4pitaux de Paris (AP-HP). Il est situ\u00e9 entre les rues Leblanc et du Professeur-Florian-Delbarre dans le 15e arrondissement de Paris, au bord de la Seine non loin du pont du Garigliano, \u00e0 proximit\u00e9 du parc Andr\u00e9-Citro\u00ebn et des locaux de France T\u00e9l\u00e9visions."
                    },
                    "2893691": {
                        "pageid": 2893691,
                        "ns": 0,
                        "title": "Rue Leblanc",
                        "index": 1,
                        "extract": "La rue Leblanc est une rue du 15e arrondissement de Paris."
                    }
                }
            }
        }

        # Result we're looking for
        results = {
            "title" : "Hôpital européen Georges-Pompidou",
            "intro" : """L'hôpital européen Georges-Pompidou (HEGP) est un hôpital de l'Assistance publique - hôpitaux de Paris (AP-HP). Il est situé entre les rues Leblanc et du Professeur-Florian-Delbarre dans le 15e arrondissement de Paris, au bord de la Seine non loin du pont du Garigliano, à proximité du parc André-Citroën et des locaux de France Télévisions.""",
            "page_link" : "https://fr.wikipedia.org/wiki/Hôpital_européen_Georges-Pompidou",
            "status" : "FOUND"
        }

        def mockreturn(request):
            return BytesIO(json.dumps(req_result).encode())

        script = MediaWikiInfo()
        monkeypatch.setattr(requests, 'Response', mockreturn)
        assert script.get_story_info(48.8388508, 2.2740328) == results

    def test_request_info_false(self, monkeypatch):
        # JSON response from the Media Wiki API
        req_result = {
            "error": {
                "code": "invalid-coord",
                "info": "Invalid coordinate provided",
                "*": "See https://fr.wikipedia.org/w/api.php for API usage. Subscribe to the mediawiki-api-announce mailing list at &lt;https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce&gt; for notice of API deprecations and breaking changes."
            },
            "servedby": "mw1287"
        }

        # Result we're looking for
        results = {
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "NOT_FOUND"
        }

        def mockreturn(request):
            return BytesIO(json.dumps(req_result).encode())

        script = MediaWikiInfo()
        monkeypatch.setattr(requests, 'Response', mockreturn)
        assert script.get_story_info(9999, 9999) == results
