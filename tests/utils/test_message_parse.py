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

    def test_remove_punctuation(self):
        assert self.PARSER.remove_punctuation(self.MESSAGE1) == "Bonjour bot Ou se trouve la Tour Eiffel"
        assert self.PARSER.remove_punctuation(self.MESSAGE2) == "Salut GrandPy Est-ce que tu connais l adresse de l Opéra de Paris"
        assert self.PARSER.remove_punctuation(self.MESSAGE3) == "Je souhaiterais aller au 59 boulevard de Strasbourg 75010 Paris s il te plaît"
        assert self.PARSER.remove_punctuation(self.MESSAGE4) == "Je veux aller visiter la cathédrale de notre-dame s il vous plait"
        assert self.PARSER.remove_punctuation(self.MESSAGE5) == "Bonjour quelle est l adresse de l hôpital Georges Pompidou"

    def test_remove_stop_words(self):
        assert self.PARSER.remove_stop_words(self.MESSAGE1) == "bonjour bot!! trouve tour eiffel?"
        assert self.PARSER.remove_stop_words(self.MESSAGE2) == "salut grandpy connais l'adresse l'opéra paris?"
        assert self.PARSER.remove_stop_words(self.MESSAGE3) == "souhaiterais aller 59 boulevard strasbourg, 75010 paris s'il plaît."
        assert self.PARSER.remove_stop_words(self.MESSAGE4) == "veux aller visiter cathédrale notre-dame s'il plait."
        assert self.PARSER.remove_stop_words(self.MESSAGE5) == "bonjour, l'adresse l'hôpital georges pompidou?"

    def test_remove_accents(self):
        assert self.PARSER.remove_accents(self.MESSAGE1) == "Bonjour bot!! Ou se trouve la Tour Eiffel?"
        assert self.PARSER.remove_accents(self.MESSAGE2) == "Salut GrandPy Est-ce que tu connais l'adresse de l'Opera de Paris?"
        assert self.PARSER.remove_accents(self.MESSAGE3) == "Je souhaiterais aller au 59 boulevard de Strasbourg, 75010 Paris s'il te plait."
        assert self.PARSER.remove_accents(self.MESSAGE4) == "Je veux aller visiter la cathedrale de notre-dame s'il vous plait."
        assert self.PARSER.remove_accents(self.MESSAGE5) == "Bonjour, quelle est l'adresse de l'hopital Georges Pompidou?"

    def test_remove_useless_words(self):
        assert self.PARSER.remove_useless_words(self.MESSAGE1) == "trouve tour eiffel"
        assert self.PARSER.remove_useless_words(self.MESSAGE2) == "connais adresse opera paris"
        assert self.PARSER.remove_useless_words(self.MESSAGE3) == "souhaiterais aller 59 boulevard strasbourg 75010 paris"
        assert self.PARSER.remove_useless_words(self.MESSAGE4) == "veux aller visiter cathedrale notre-dame"
        assert self.PARSER.remove_useless_words(self.MESSAGE5) == "adresse hopital georges pompidou"

    def test_split_by_keywords(self):
        assert self.PARSER.split_by_keywords(self.MESSAGE1) == "la tour eiffel?"
        assert self.PARSER.split_by_keywords(self.MESSAGE2) == "de l'opéra de paris?"
        assert self.PARSER.split_by_keywords(self.MESSAGE3) == "au 59 boulevard de strasbourg, 75010 paris s'il te plaît."
        assert self.PARSER.split_by_keywords(self.MESSAGE4) == "la cathédrale de notre-dame s'il vous plait."
        assert self.PARSER.split_by_keywords(self.MESSAGE5) == "de l'hôpital georges pompidou?"

    # Keep only this test in the end
    def test_identify_location(self):
        assert self.PARSER.identify_location(self.MESSAGE1) == "tour eiffel"
        assert self.PARSER.identify_location(self.MESSAGE2) == "opera paris"
        assert self.PARSER.identify_location(self.MESSAGE3) == "59 boulevard strasbourg 75010 paris"
        assert self.PARSER.identify_location(self.MESSAGE4) == "cathedrale notre-dame"
        assert self.PARSER.identify_location(self.MESSAGE5) == "hopital georges pompidou"
