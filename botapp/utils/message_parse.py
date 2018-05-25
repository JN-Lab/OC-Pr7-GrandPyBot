#! /usr/bin/env python3
# coding: utf-8
import unicodedata
import re
from string import punctuation
from .stop_words import common_words, welcome_words

class MessageParser:

    def remove_punctuation(self, message):
        final_message = []
        for letter in message:
            if letter not in punctuation or letter == "-":
                final_message.append(letter)
            else:
                if letter == "'":
                    letter = " "
                    final_message.append(letter)

        final_message = ''.join(final_message)

        return final_message

    def remove_stop_words(self, message):
        # probleme sur lalgo quand on doit supprimer deux mots qui se suivent. Logique...
        split_message = message.lower().split()
        final_message = []
        print(split_message)
        for word in split_message:
            if word not in common_words:
                final_message.append(word)
        final_message = ' '.join(final_message)
        return final_message

    def remove_accents(self, message):
        try:
            message = unicode(message, 'utf-8')
        except NameError:
            pass
        message = unicodedata.normalize('NFD', message)
        message = message.encode('ascii', 'ignore')
        message = message.decode('utf-8')
        return str(message)

    def remove_useless_words(self, message):
        message.lower()
        message = self.remove_punctuation(message)
        message = self.remove_accents(message)
        message = self.remove_stop_words(message)
        split_message = message.split()
        final_message = []
        for word in split_message:
            if word not in welcome_words:
                final_message.append(word)

        final_message =' '.join(final_message)
        return final_message

    def remove_location_keywords(self, message):
        message = message.lower().split()
        final_message = []
        for word in message:
            final_message.append(word)
            match = re.search(r'\'?ad+res+e|trouve|^con+ai|^visi|^al+e|^voi[r|s]|^sa[is|v]|^voudrais|^veu[x|s]|^souhait', word)
            if match:
                final_message = []
        final_message = ' '.join(final_message)
        return final_message

    def remove_question_structure(self, message):
        pass
