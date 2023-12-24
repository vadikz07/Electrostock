import webbrowser
import re

pattern = "(https?:\/\/).*"

def open_dsheet_url(url_string='http://www.thisisatest.com/testing'):
    if url_string and re.match(pattern, url_string):
        print(f'Abriendo {url_string}')
        webbrowser.open(url_string)
        
    else:
        print('url vacia')
        return 1

def validate_url(url_string):
    if re.match(pattern, url_string):
        return True
    return False