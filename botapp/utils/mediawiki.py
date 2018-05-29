#! /usr/bin/env python3
# coding: utf-8
import requests

class MediaWikiInfo:

    def get_story_info(self, latitude, longitude):
        pass

"""
https://fr.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&generator=geosearch&ggscoord=48.8388508|2.2740328&ggsradius=100&contentmodel=json
"""

"""
https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&generator=geosearch&ggscoord=48.8388508|2.2740328&ggsradius=100
"""

"""
https://fr.wikipedia.org/w/api.php?action=parse&text=%7B%7B%5Cu00c9bauche%7Ch%5Cu00f4pital%7CParis%7D%7D%5Cn%7B%7BInfobox%20H%5Cu00f4pital%5Cn%20%7C%20nom%20%20%20%20%20%20%20%20%20%20%20%20%3D%20H%5Cu00f4pital%20europ%5Cu00e9en%20Georges-Pompidou%5Cn%20%7C%20logo%20%20%20%20%20%20%20%20%20%20%20%3D%20%5Cn%20%7C%20logo%20taille%20%20%20%20%3D%20%5Cn%20%7C%20image%20%20%20%20%20%20%20%20%20%20%3D%20H%5Cu00f4pital%20europ%5Cu00e9en%20Georges-Pompidou%20logo.JPG%5Cn%20%7C%20l%5Cu00e9gende%20%20%20%20%20%20%20%20%3D%20Logo%20de%20l%27%5B%5BAssistance%20publique%20-%20h%5Cu00f4pitaux%20de%20Paris%5D%5D%20sur%20l%27H%5Cu00f4pital%20europ%5Cu00e9en%20Georges-Pompidou%5Cn%20%7C%20longitude%20%20%20%20%20%20%3D%202.2737%5Cn%20%7C%20latitude%20%20%20%20%20%20%20%3D%2048.8389%5Cn%20%7C%20pays%20%20%20%20%20%20%20%20%20%20%20%3D%20%7B%7BFrance%7D%7D%5Cn%20%7C%20ville%20%20%20%20%20%20%20%20%20%20%3D%20%5B%5BParis%5D%5D%5Cn%20%7C%20adresse%20%20%20%20%20%20%20%20%3D%2020%2C%20%5B%5Brue%20Leblanc%5D%5D%2075015%5Cn%20%7C%20date%20fondation%20%3D%20%5B%5B2001%5D%5D%5Cn%20%7C%20date%20fermetsure%20%3D%20%5Cn%20%7C%20site%20web%20%20%20%20%20%20%20%3D%20http%3A%2F%2Fhopital-georgespompidou.aphp.fr%2F%5Cn%20%7C%20type%20%20%20%20%20%20%20%20%20%20%20%3D%20%5Cn%20%7C%20assurance%20mal%20%20%3D%20%5Cn%20%7C%20affiliation%20%20%20%20%3D%20%5B%5BAssistance%20publique%20-%20h%5Cu00f4pitaux%20de%20Paris%7CAP-HP%5D%5D%20%5Cn%20%7C%20sta&contentmodel=wikitext&contentformat=text/plain
"""

"""
Good One
https://fr.wikipedia.org/w/api.php?action=query&prop=extracts|url&exintro&explaintext&generator=geosearch&ggscoord=48.8388508|2.2740328&ggsradius=100
"""
