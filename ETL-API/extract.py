import requests, pandas as pd
import json
import sys
from api_limit_call import check_api_limit

class Url:
    """
    A class used to represent a URL

    Attributes
    ----------
    file_name: str
        the name of the file name 
        
    Methods
    
    --------
    read_json_file()
        read any json file 
    """
    
    file_name  = None
    def __init__(self) -> None:
        self.file_name = sys.argv[1]
        
    def read_json_file(self):
        json_file = open(self.file_name)
        json_data = json.load(json_file)
        url = json_data['url']
        return url

    
class ExtractData(Url):
    """
    A class used to extract data

    Attributes
    ----------
    url: str
        the http link to the web api
        
    Methods
    
    --------
    extract_data()
        extracts json file from the url
    """
    
    def __init__(self, url: Url) -> None:
        self.url = url
        
    def extract_data(self):
        # call the api limiter
        check_api_limit()
        res = requests.get(self.url)
        items = res.json()

        return items



# if __name__ == "__main__":
#     url = Url()
#     url_link = url.read_json_file()
#     extract = ExtractData(url_link)
#     print(extract.extract_data())
    
    
