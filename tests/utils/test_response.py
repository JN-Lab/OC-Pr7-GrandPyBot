#! /usr/bin/env python3
# coding: utf-8
from botapp.utils.response import Response

class TestReponse:

    ANALYSE = Response()

    def test_response_success(self, monkeypatch):
        #geocoding dict return
        geocoding_results = {
            "address" : "20 Rue Leblanc, 75015 Paris, France",
            "latitude" : 48.8388508,
            "longitude" : 2.2740328,
            "status" : "FOUND"
        }
        #wiki media dict return
        mediawiki_results = {
            "title" : "Hôpital européen Georges-Pompidou",
            "intro" : """L'hôpital européen Georges-Pompidou (HEGP) est un hôpital de l'Assistance publique - hôpitaux de Paris (AP-HP). Il est situé entre les rues Leblanc et du Professeur-Florian-Delbarre dans le 15e arrondissement de Paris, au bord de la Seine non loin du pont du Garigliano, à proximité du parc André-Citroën et des locaux de France Télévisions.""",
            "page_link" : "https://fr.wikipedia.org/wiki/Hôpital_européen_Georges-Pompidou",
            "status" : "FOUND"
        }
        #result expected
        results = {
            "address" : "20 Rue Leblanc, 75015 Paris, France",
            "latitude" : 48.8388508,
            "longitude" : 2.2740328,
            "title" : "Hôpital européen Georges-Pompidou",
            "intro" : """L'hôpital européen Georges-Pompidou (HEGP) est un hôpital de l'Assistance publique - hôpitaux de Paris (AP-HP). Il est situé entre les rues Leblanc et du Professeur-Florian-Delbarre dans le 15e arrondissement de Paris, au bord de la Seine non loin du pont du Garigliano, à proximité du parc André-Citroën et des locaux de France Télévisions.""",
            "page_link" : "https://fr.wikipedia.org/wiki/Hôpital_européen_Georges-Pompidou",
            "status" : "COMPLETE"
        }

        assert self.ANALYSE.get_info("Bonjour, quelle est l'adresse de l'hôpital Georges Pompidou?") == results

    def test_response_false_missing_location(self):

        results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "LOCATION_MISSING"
        }

        assert self.ANALYSE.get_info("Bonjour, comment allez-vous") == results

    def test_response_false_missing_geographic_info(self):

        results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "WRONG_LOCATION"
        }

        assert self.ANALYSE.get_info("Bonjour, quelle est l'adresse de fake location?") == results

    def test_response_false_missing_story_info(self):
        results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "STORY_MISSING"
        }

        assert self.ANALYSE.get_info("Bonjour, je souhaite me rendre à eulerian?") == results
