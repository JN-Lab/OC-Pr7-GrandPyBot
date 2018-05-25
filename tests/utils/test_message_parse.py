#! /usr/bin/env python3
# coding: utf-8
from botapp.utils.message_parse import MessageParser

class TestMessageParser:
    MESSAGE1 = "Bonjour bot!! Ou se trouve la Tour Eiffel?"
    MESSAGE2 = "Salut GrandPy Est-ce que tu connais l'adresse de l'Opéra de Paris?"
    MESSAGE3 = "Je souhaiterais aller au 59 boulevard de Strasbourg, 75010 Paris s'il te plaît."
    MESSAGE4 = "Je veux allez visiter la cathédrale de notre-dame s'il vous plait."
    MESSAGE5 = "Bonjour, quelle est l'adresse de l'hôpital Georges Pompidou?"

    PARSER = MessageParser()

    def test_remove_punctuation(self):
        assert self.PARSER.remove_punctuation(self.MESSAGE1) == "Bonjour bot Ou se trouve la Tour Eiffel"
        assert self.PARSER.remove_punctuation(self.MESSAGE2) == "Salut GrandPy Est ce que tu connais l adresse de l Opéra de Paris"
        assert self.PARSER.remove_punctuation(self.MESSAGE3) == "Je souhaiterais aller au 59 boulevard de Strasbourg 75010 Paris s il te plaît"
        assert self.PARSER.remove_punctuation(self.MESSAGE4) == "Je veux allez visiter la cathédrale de notre dame s il vous plait"
        assert self.PARSER.remove_punctuation(self.MESSAGE5) == "Bonjour quelle est l adresse de l hôpital Georges Pompidou"

    def test_remove_useless_words(self):
        assert self.PARSER.remove_useless_words(self.MESSAGE1) == "bonjour bot!! trouve tour eiffel?"
        assert self.PARSER.remove_useless_words(self.MESSAGE2) == "salut grandpy connais l'adresse l'opéra paris?"
        assert self.PARSER.remove_useless_words(self.MESSAGE3) == "souhaiterais aller 59 boulevard strasbourg, 75010 paris s'il plaît."
        assert self.PARSER.remove_useless_words(self.MESSAGE4) == "veux allez visiter cathédrale notre-dame s'il plait."
        assert self.PARSER.remove_useless_words(self.MESSAGE5) == "bonjour, l'adresse l'hôpital georges pompidou?"

    def test_remove_accents(self):
        assert self.PARSER.remove_accents(self.MESSAGE1) == "Bonjour bot!! Ou se trouve la Tour Eiffel?"
        assert self.PARSER.remove_accents(self.MESSAGE2) == "Salut GrandPy Est-ce que tu connais l'adresse de l'Opera de Paris?"
        assert self.PARSER.remove_accents(self.MESSAGE3) == "Je souhaiterais aller au 59 boulevard de Strasbourg, 75010 Paris s'il te plait."
        assert self.PARSER.remove_accents(self.MESSAGE4) == "Je veux allez visiter la cathedrale de notre-dame s'il vous plait."
        assert self.PARSER.remove_accents(self.MESSAGE5) == "Bonjour, quelle est l'adresse de l'hopital Georges Pompidou?"

    # remove_useless_words + remove_punctuation + remove_accents integrated in function
    def test_remove_civilities(self):
        assert self.PARSER.remove_civilities(self.MESSAGE1) == "trouve tour eiffel"
        assert self.PARSER.remove_civilities(self.MESSAGE2) == "connais adresse opera paris"
        assert self.PARSER.remove_civilities(self.MESSAGE3) == "souhaiterais aller 59 boulevard strasbourg 75010 paris"
        assert self.PARSER.remove_civilities(self.MESSAGE4) == "veux allez visiter cathedrale dame"
        assert self.PARSER.remove_civilities(self.MESSAGE5) == "adresse hopital georges pompidou"
