from bs4 import BeautifulSoup
import re
import parser

def parse_lutz():
    """

    """    
    
    # Volume 1   
    # Read the source html file and strip out the text.
    file = open('/home/jack/Downloads/simple.html', 'r')
    raw_text = file.read()
    bs4_text = BeautifulSoup(raw_text, 'lxml')
    book = bs4_text.getText()
    
    # Cretae a list of articles by splitting them based on
    # [number]:. Articles begin at location 39846.
    vol1 = re.split("\[\d+\]: ", book[39846:])
    vol1 = vol1[1:]

    # Volume 2   
    file = open('/home/jack/Downloads/simple2.html', 'r')
    raw_text = file.read()
    bs4_text = BeautifulSoup(raw_text, 'lxml')
    book = bs4_text.getText()
    
    # Articles begin at location 19326.
    vol2 = re.split("\[\d+\]: ", book[19326:])
    vol2 = vol2[1:]
    
    # We want to combine volumes.
    articles = vol1 + vol2
    
    # Each article will be broken down into author,
    # title, location, year, background, and content.
    lutz_books = []
    for article in articles:
        lutz_books.append(parser.parse_lutz_book(article))
    
    return lutz_books