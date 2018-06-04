#! /usr/bin/env python3
# coding: utf-8
from botapp.utils.response import Response

class TestReponse:
    """
    This class tests the results get after the use of the method get_info from
    Response class.
    """

    ANALYSE = Response()

    def test_response_success(self, monkeypatch):
        """
        This method tests the success path
        """

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

        def mock_get_location_info(location):
            return geocoding_results

        def mock_get_story_info(latitude, longitude):
            return mediawiki_results

        monkeypatch.setattr(self.ANALYSE.gps_seeker, 'get_location_info', mock_get_location_info)
        monkeypatch.setattr(self.ANALYSE.story_seeker, 'get_story_info', mock_get_story_info)

        assert self.ANALYSE.get_info("Bonjour, quelle est l'adresse de l'hôpital Georges Pompidou?") == results

    def test_response_false_missing_location(self, monkeypatch):
        """
        This method tests the path where the message parser returns nothing
        """

        #parse feature return
        parse_result = ""

        #result expected
        results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "LOCATION_MISSING"
        }

        def mock_get_message_parsed(message):
            return parse_result

        monkeypatch.setattr(self.ANALYSE.message_parser, 'identify_location', mock_get_message_parsed)

        assert self.ANALYSE.get_info("Bonjour, comment allez-vous") == results

    def test_response_false_missing_geographic_info(self, monkeypatch):
        """
        This method tests the path where the Google geoconding api doesn't
        return a precise location
        """

        #geocoding dict return
        geocoding_results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "status" : "NOT_FOUND"
        }

        #result expected
        results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "WRONG_LOCATION"
        }

        def mock_get_location_info(location):
            return geocoding_results

        monkeypatch.setattr(self.ANALYSE.gps_seeker, 'get_location_info', mock_get_location_info)

        assert self.ANALYSE.get_info("Bonjour, quelle est l'adresse de fake location?") == results

    def test_response_false_missing_story_info(self, monkeypatch):
        """
        This method tests the path where the wikimedia API doesn't return
        a story
        """

        #geocoding dict return
        geocoding_results = {
            "address" : "20 Rue Leblanc, 75015 Paris, France",
            "latitude" : 48.8388508,
            "longitude" : 2.2740328,
            "status" : "FOUND"
        }
        #wiki media dict return
        mediawiki_results = {
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "NOT_FOUND"
        }

        #result expected
        results = {
            "address" : "20 Rue Leblanc, 75015 Paris, France",
            "latitude" : 48.8388508,
            "longitude" : 2.2740328,
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "STORY_MISSING"
        }

        def mock_get_location_info(location):
            return geocoding_results

        def mock_get_story_info(latitude, longitude):
            return mediawiki_results

        monkeypatch.setattr(self.ANALYSE.gps_seeker, 'get_location_info', mock_get_location_info)
        monkeypatch.setattr(self.ANALYSE.story_seeker, 'get_story_info', mock_get_story_info)

        assert self.ANALYSE.get_info("Bonjour, je souhaite me rendre à eulerian?") == results

    def test_response_false_request_problem_location(self, monkeypatch):
        """
        This method tests the path where there is a request problem with
        Google geocoding API
        """

        geocoding_results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "status" : "REQUEST_PROBLEM"
        }

        results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "GOOGLE_GEOCODING_API_PROBLEM"
        }

        def mock_get_location_info(location):
            return geocoding_results

        monkeypatch.setattr(self.ANALYSE.gps_seeker, 'get_location_info', mock_get_location_info)

        assert self.ANALYSE.get_info("Bonjour, quelle est l'adresse de la tour eiffel?") == results

    def test_response_false_request_problem_story(self, monkeypatch):
        """
        This method tests the path where there is a request problem with
        Wikimedia API
        """
        #geocoding dict return
        geocoding_results = {
            "address" : "20 Rue Leblanc, 75015 Paris, France",
            "latitude" : 48.8388508,
            "longitude" : 2.2740328,
            "status" : "FOUND"
        }
        #wiki media dict return
        mediawiki_results = {
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "REQUEST_PROBLEM"
        }

        #result expected
        results = {
            "address" : "20 Rue Leblanc, 75015 Paris, France",
            "latitude" : 48.8388508,
            "longitude" : 2.2740328,
            "title" : "",
            "intro" : "",
            "page_link" : "",
            "status" : "WIKIMEDIA_API_PROBLEM"
        }

        def mock_get_location_info(location):
            return geocoding_results

        def mock_get_story_info(latitude, longitude):
            return mediawiki_results

        monkeypatch.setattr(self.ANALYSE.gps_seeker, 'get_location_info', mock_get_location_info)
        monkeypatch.setattr(self.ANALYSE.story_seeker, 'get_story_info', mock_get_story_info)

        assert self.ANALYSE.get_info("Bonjour, je souhaite me rendre au Trocadéro?") == results
