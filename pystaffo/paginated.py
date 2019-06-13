import requests
import json

per_page = 300

def get(auth=None, url=None, extras=None):
    """
    Paginated GET
    """
    data = []
    keep_going = True
    page = 1 # start with page = 1. thats the first page
    params = {'page': page, 'per_page': per_page}
    if extras:
        params.update(extras)
    r = requests.get(url=url, auth=auth, params=params)
    response = json.loads(r.content.decode('utf-8'))
    data = response
    if len(response) == 0 or (not 'Page' in r.headers): # if the API returns an empty array or no pages, we know we dont have any data left
        keep_going = False
    while keep_going: # keep iterating over pages until `keep_going == false`
        page += 1
        params.update({'page': page}) 
        r = requests.get(url=url, auth=auth, params=params)
        response = json.loads(r.content.decode('utf-8'))
        if len(response) == 0:
            keep_going = False
        else:
            data += response
    return data

    