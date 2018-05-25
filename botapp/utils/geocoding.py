#! /usr/bin/env python3
# coding: utf-8
from config import Config
import requests

class GeocodingLocation:

    def __init__(self, location):
        self.location = location
        api_key = Config.GEOCODING_GOOGLE_API_KEY
