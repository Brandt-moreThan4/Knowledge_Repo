from bs4 import BeautifulSoup
# from selenium import webdriver
import requests
import time
import string
# from pathlib import Path


def get_page_response(url):
    """Get a page response using the given url"""
    try:
        page_response = requests.get(url)
    except:
        print('Error loading url')
        return None
    else:
        return page_response

def get_soup(url: str):
    """Returns beautiful Soup object of the requested page or None if there was trouble somehwere along the way."""

    page_response = get_page_response(url)
    if page_response is not None:
        try:
            soup = BeautifulSoup(page_response.text)
        except:
            print('Trouble parsing the soup for: {}'.format(url))
            return None
        else:
            return soup
    else:
        print('The response object was "None" so there is no point in trying to parse')
        return None


def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
    Uses a whitelist approach: any characters not present in valid_chars are
    removed. Also spaces are replaced with underscores.
    """
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    return filename



def time_usage(func):
    """I think this function can be used as a decorator on any other function which will return the time for the decorated function to run."""
    def wrapper(*args, **kwargs):
        begin_time = time.time()
        retval = func(*args, **kwargs)
        end_time = time.time()
        print(f"elapsed time: {(end_time - begin_time)}")
        return retval

    return wrapper
