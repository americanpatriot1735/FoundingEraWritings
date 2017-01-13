# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:15:41 2016

@author: jack
"""

class Book_Lutz:
    def __init__(self, author, title, location, year, background, content):
        self._author = author
        self._title = title
        self._location = location
        self._year = year
        self._background = background
        self._content = content
    
    @property
    def author(self):
        return self._author
        
    @property
    def title(self):
        return self._title
    
    @property
    def location(self):
        return self._location
        
    @location.setter
    def location(self, value):
        self._location = value
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value
    
    @property
    def background(self):
        return self._background
    
    @property
    def content(self):
        return self._content