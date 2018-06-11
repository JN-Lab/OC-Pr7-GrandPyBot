#! /usr/bin/env python3
# coding: utf-8
from botapp.utils.message_parse import MessageParser

class TestMessageParser:
    MESSAGE1 = "Bonjour bot!! Ou se trouve la Tour Eiffel?"
    MESSAGE2 = "Salut GrandPy Est-ce que tu connais l'adresse de l'Opéra de Paris?"
    MESSAGE3 = "Je souhaiterais aller au 59 boulevard de Strasbourg, 75010 Paris s'il te plaît."
    MESSAGE4 = "Je veux aller visiter la cathédrale de notre-dame s'il vous plait."
    MESSAGE5 = "Bonjour, quelle est l'adresse de l'hôpital Georges Pompidou?"

    PARSER = MessageParser()

    def test_identify_location(self):
        assert self.PARSER.identify_location(self.MESSAGE1) == "tour eiffel"
        assert self.PARSER.identify_location(self.MESSAGE2) == "opera paris"
        assert self.PARSER.identify_location(self.MESSAGE3) == "59 boulevard strasbourg 75010 paris"
        assert self.PARSER.identify_location(self.MESSAGE4) == "cathedrale notre-dame"
        assert self.PARSER.identify_location(self.MESSAGE5) == "hopital georges pompidou"
