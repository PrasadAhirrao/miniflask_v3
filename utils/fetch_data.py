import requests
from typing import Tuple
from utils.logger import logger
from utils.timeit import timeit
from pprint import pprint


@timeit
@logger
def fetch_data(url: str) -> Tuple:
    """
    Returns tuple of response object and response in json format received from
    requests.get() function, for given url
    :param url: to send HTTP request
    :return: Tuple (response object, response in json format)
    """
    response = requests.get(url)  # response object
    # response = response_obj.json()    # converting json
    return response
