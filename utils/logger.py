
def logger(func):
    """
    decorator for logging details of url and status code
    :param func: function which hits API endpoint
    :return: json response
    """
    def wrapper(url, *args, **kwargs):
        print(f"Fetching details from - {url} =>")
        result = func(url)
        print(f"Status: {result.status_code} - [{result.reason}]")
        return result.json()
    return wrapper