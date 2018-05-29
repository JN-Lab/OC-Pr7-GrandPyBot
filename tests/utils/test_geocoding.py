#! /usr/bin/env python3
# coding: utf-8
from botapp.utils.geocoding import GeocodingLocation
import requests
from io import BytesIO
import json

class TestGeocodingLocation:
    """
    This class tests the results get after requesting Google Geocoding API.
    There are two tests:
        - One with coming from a request with a real location
        - One with coming from a request with a non real location
    """

    def test_request_address_success(self, monkeypatch):
        """
        This methods tests the result coming from a request with a real location.
        The monkeypatch fixture is used to simulate the response -> req_result
        """

        # JSON response from the Google Geocoding API
        req_result = {
            "results" : [
                {
                    "formatted_address" : "20 Rue Leblanc, 75015 Paris, France",
                    "geometry" : {
                        "location" : {
                            "lat" : 48.8388508,
                            "lng" : 2.2740328
                        },
                    "location_type" : "ROOFTOP",
                    },

                }
            ],
        }

        # Result we're looking for
        results = {
            "address" : "20 Rue Leblanc, 75015 Paris, France",
            "latitude" : 48.8388508,
            "longitude" : 2.2740328,
            "status" : "found"
        }

        def mockreturn(request):
            return BytesIO(json.dumps(req_result).encode())

        script = GeocodingLocation()
        monkeypatch.setattr(requests, 'Response', mockreturn)
        assert script.get_location_info("hopital georges pompidou") == results

    def test_request_address_false(self, monkeypatch):
        """
        This methods tests the result coming from a request with a non real location.
        The monkeypatch fixture is used to simulate the response -> req_result
        """

        # JSON response from the Google Geocoding API
        req_result = {
            "results" : [
                {
                    "formatted_address" : "France",
                    "geometry" : {
                        "location" : {
                            "lat" : 46.227638,
                            "lng" : 2.213749
                        },
                    "location_type" : "APPROXIMATE",
                    },

                }
            ],
        }

        # Result we're looking for
        results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "status" : "not_found"
        }

        def mockreturn(request):
            return json.JSONEncoder().encode(req_result)

        req = GeocodingLocation()
        monkeypatch.setattr(requests, 'Response', mockreturn)
        assert req.get_location_info("fake location") == results
