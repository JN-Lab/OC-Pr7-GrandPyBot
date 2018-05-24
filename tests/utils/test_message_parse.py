#! /usr/bin/env python3
# coding: utf-8
from botapp.utils.message_parse import MessageParser

class TestMessageParser:
    MESSAGE1 = "Bonjour bot!! Ou se trouve la Tour Eiffel?"
    MESSAGE2 = "Salut GrandPy Est-ce que tu connais l'adresse de l'Opera de Paris?"
    MESSAGE3 = "Je souhaiterais aller au 59 boulevard de Strabourg, 75010 Paris s'il te plait."
    MESSAGE4 = "Je veux allez visiter la cathédrale de notre-dame s'il vous plait."
    MESSAGE5 = "Bonjour, quelle est l'adresse de l'hopital Georges Pompidou?"

    PARSER = MessageParser()

    def test_remove_punctuation(self):
        assert self.PARSER.remove_punctuation(self.MESSAGE1) == "Bonjour bot Ou se trouve la Tour Eiffel"
        assert self.PARSER.remove_punctuation(self.MESSAGE2) == "Salut GrandPy Estce que tu connais ladresse de lOpera de Paris"
        assert self.PARSER.remove_punctuation(self.MESSAGE3) == "Je souhaiterais aller au 59 boulevard de Strabourg 75010 Paris sil te plait"
        assert self.PARSER.remove_punctuation(self.MESSAGE4) == "Je veux allez visiter la cathédrale de notredame sil vous plait"

    def test_remove_useless_words(self):
        assert self.PARSER.remove_useless_words(self.MESSAGE1) == "bonjour bot!! trouve tour eiffel?"
        assert self.PARSER.remove_useless_words(self.MESSAGE2) == "salut grandpy tu connais adresse opera paris?"
        assert self.PARSER.remove_useless_words(self.MESSAGE3) == "souhaiterais aller 59 boulevard strabourg, 75010 paris s'il plait."
        assert self.PARSER.remove_useless_words(self.MESSAGE4) == "veux allez visiter cathédrale notre-dame s'il plait."

    # remove_useless_words + remove_punctuation integrated in function
    def test_remove_civilities(self):
        assert self.PARSER.remove_civilities(self.MESSAGE1) == "ou se trouve la tour eiffel"
        assert self.PARSER.remove_civilities(self.MESSAGE2) == "est-ce que tu connais l'adresse de l'opera de paris?"
        assert self.PARSER.remove_civilities(self.MESSAGE3) == "je souhaiterais aller au 59 boulevard de strabourg, 75010 paris."
        assert self.PARSER.remove_civilities(self.MESSAGE4) == "je veux allez visiter la cathédrale de notre-dame s'il vous plait."
