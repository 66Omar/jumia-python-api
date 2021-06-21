import urllib.parse
from hashlib import sha256
from hmac import HMAC
import json
import requests


def get_data(api_key, parameters):
    parameters = {k: v for k, v in sorted(parameters.items()) if v is not None}
    concatenated = urllib.parse.urlencode(parameters)
    parameters['Signature'] = HMAC(api_key.encode(), concatenated.encode('utf-8'), sha256).hexdigest()
    concatenated = urllib.parse.urlencode(parameters)
    site = 'https://sellercenter-api.jumia.com.eg/'
    final_link = site + "?" + concatenated
    json_data = requests.get(final_link)
    data_dict = json.loads(json_data.content)
    return data_dict
