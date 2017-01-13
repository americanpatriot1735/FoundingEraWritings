# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:15:17 2016

@author: jack
"""
from books import Book_Lutz

def parse_lutz_book(book):
    """
    
    """
    # Parse the author.
    old_loc = 0
    new_loc = book.find('\n\n', old_loc)
    author = book[old_loc:new_loc]
    old_loc = new_loc + 1

    # Parse the title.
    new_loc = book.find('\n\n', old_loc)
    title = book[old_loc+1:new_loc]
    old_loc = new_loc + 1
    
    # Parse the location and the year.
    new_loc = book.find('\n\n', old_loc)
    line = book[old_loc:new_loc]
    location = line[:-5].replace(',', '')
    year = line[-4:]
    old_loc = new_loc + 1
    
    # The articles include a background that will be saved
    # for later use.
    new_loc = book.find('\n\n', old_loc)
    background = book[old_loc+1:new_loc]
    old_loc = new_loc + 1
    
    # Parse the content of the article
    new_loc = book.find('\n\n', old_loc)
    content = book[old_loc+1:]
    
    bc = Book_Lutz(author, title, location, year, background, content)
    
    return bc