#! /usr/bin/env python3
# coding: utf-8
from string import punctuation
from .stop_words import common_words, welcome_words

class MessageParser:

    def remove_punctuation(self, message):
        message = ''.join([letter for letter in message if letter not in punctuation])
        return message

    def remove_useless_words(self, message):
        # probleme sur lalgo quand on doit supprimer deux mots qui se suivent. Logique...
        split_message = message.lower().split()
        print(split_message)
        for word in split_message:
            if word in common_words:
                split_message.remove(word)

        final_message = ' '.join(split_message)
        return final_message

    def remove_civilities(self, message):
        # Meme probleme qu'au dessus
        message = self.remove_punctuation(message)
        split_message = message.lower().split()
        print(split_message)
        for word in split_message:
            if word in welcome_words:
                split_message.remove(word)

        final_message = ' '.join(split_message)
        return final_message
