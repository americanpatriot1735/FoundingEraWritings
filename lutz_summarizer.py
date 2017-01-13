# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:38:56 2016

@author: jack
"""

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

#from susmy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from lutz_munge import parse_lutz

SENTENCES_COUNT = 10
LANGUAGE = "english"

if __name__ == "__main__":
    #url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
    #parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    
    lutz_books = parse_lutz()
    
    for article in iter(lutz_books):
        print(article.author.upper())
        parser = PlaintextParser.from_string(article.content, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE) | frozenset(['edition','page','1983'])
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            print(sentence)