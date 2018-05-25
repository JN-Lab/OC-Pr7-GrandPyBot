#! /usr/bin/env python3
# coding: utf-8
from botapp.utils.geocoding import GeocodingLocation

class TestGeocodingLocation:

    def test_request_address_success(self, monkeypatch):
        {
           "results" : [
              {
                 "formatted_address" : "20 Rue Leblanc, 75015 Paris, France",
                 "geometry" : {
                    "location" : {
                       "lat" : 48.8388508,
                       "lng" : 2.2740328
                    },
                 },
              }
           ],
           "status" : "OK"
        }
        pass
