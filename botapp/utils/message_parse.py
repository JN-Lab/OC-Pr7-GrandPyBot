#! /usr/bin/env python3
# coding: utf-8
import unicodedata
import re
from string import punctuation
from .stop_words import common_words, welcome_words

class MessageParser:
    """
    This class is one of the main treatment of this programm.
    It is used to identify the location the user is looking for from his message.
    """

    def remove_punctuation(self, message):
        """This method removes the punctuation from a message"""
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
        """
        This method removes words from a message
        according free useless stop words list
        """
        split_message = message.lower().split()
        final_message = []
        for word in split_message:
            if word not in common_words:
                final_message.append(word)
        final_message = ' '.join(final_message)
        return final_message

    def remove_accents(self, message):
        """This method removes the accent from a message"""
        try:
            message = unicode(message, 'utf-8')
        except NameError:
            pass
        message = unicodedata.normalize('NFD', message)
        message = message.encode('ascii', 'ignore')
        message = message.decode('utf-8')
        return str(message)

    def remove_useless_words(self, message):
        """
        This method removes all the useless words from a message
        It includes different methods from MessageParser class.
        First, it cleans message by removing punctuation and accents.
        Secondly, it cleans message by removing common words from a free list.
        Finally, it removes all the welcome words.
        """
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

    def split_by_keywords(self, message):
        """
        This method cleans a message asking a location by targeting specific
        keywords linked to this kind of message and remove all the previous words
        from it
        """
        message = message.lower().split()
        final_message = []
        for word in message:
            final_message.append(word)
            match = re.search(r'\'?ad+res+e|trouve|^con+ai|^visi|^al+e|^voi[r|s]|^sa[is|v]|^voudrais|^veu[x|s]|^souhait', word)
            if match:
                final_message = []
        final_message = ' '.join(final_message)
        return final_message

    def identify_location(self, message):
        """
        This is the global method integrating all the treatment methods from
        this class. It is the public method that will be used in the programm.
        """
        message = self.split_by_keywords(message)
        message = self.remove_useless_words(message)

        return message
