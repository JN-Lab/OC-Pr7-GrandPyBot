#! /usr/bin/env python3
# coding: utf-8
from string import punctuation
from .stop_words import common_words, welcome_words

class MessageParser:

    def remove_punctuation(self, message):
        message = ''.join([letter for letter in message if letter not in punctuation])
        return message

    def remove_useless_words(self, message):
        split_message = message.lower().split()
        for word in split_message:
            if word in common_words:
                split_message.remove(word)

        final_message = ' '.join(split_message)
        return final_message

    def remove_civilities(self):
        welcome_word = ["bonjour", "salut", "bonsoir", "hello", "hi", "coucou",
                        "grandpy", "bot", "programme", "application", "robot",
                        "s'il te plait", "s'il vous plait", "please", "svp", "merci"]
