#! /usr/bin/env python3
# coding: utf-8
from botapp.utils.geocoding import GeocodingLocation
import requests

class TestGeocodingLocation:

    def test_request_address_success(self, monkeypatch):
        results = {
            "address" : "20 Rue Leblanc, 75015 Paris, France",
            "latitude" : 48.8388508,
            "longitude" : 2.2740328,
            "status" : "found"
        }

        def mockreturn(request):
            return results

        req = GeocodingLocation()
        assert req.get_location_info("hopital georges pompidou") == results

    def test_request_address_false(self, monkeypatch):
        results = {
            "address" : "",
            "latitude" : 0,
            "longitude" : 0,
            "status" : "not found"
        }

        def mockreturn(request):
            return results

        req = GeocodingLocation()
        assert req.get_location_info("fake location") == results
