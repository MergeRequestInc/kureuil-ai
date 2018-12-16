#!/usr/bin/python3

from confFile import return_token
import requests
import json
import sys
 
ENTITY_URL = 'https://api.dandelion.eu/datatxt/nex/v1'
 
def get_entities(url, confidence=0.9):
    payload = {
        'token': return_token(),
        'url': url,
        'confidence': confidence,
        'social.hashtag': True,
        'social.mention': True
    }
    response = requests.get(ENTITY_URL, params=payload)
    return response.json()
 
def print_entities(data):
    for annotation in data['annotations']:
        print("Entity found: %s" % annotation['spot'])
 
if __name__ == '__main__':
    response = get_entities(sys.argv[1])
    print_entities(response)
