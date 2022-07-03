import requests
import sys
#import logging  # remove this for debugging purposes
from requests.auth import HTTPBasicAuth

headers = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) Chrome/103.0.0.0 Mobile','content-type':'application/json'}
cookies = dict(m='2258:Z3Vlc3Q6Z3Vlc3Q=')
basic = HTTPBasicAuth('guest', 'guest')

def get_status(url):
    r = requests.get(url + '/api/whoami', headers=headers, cookies=cookies, auth=basic)
    print(url, r.status_code, r.text)

# remove """ for debugging purposes
"""
try:
    import http.client as http_client
except ImportError:
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
"""

if __name__  == "__main__":
    file = open(sys.argv[1], 'r')
    
    for url in file:
        url = url.rstrip('\n');
        get_status(url)
