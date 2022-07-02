import requests
import sys

def get_status(url):
    headers = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36', 'content-type': 'application/json', 'authorization': 'Basic Z3Vlc3Q6Z3V0ZXN0', 'Cookie': 'm=2258:Z3Vlc3Q6Z3V0ZXN0', 'Host': 'alert-spider.rmq.cloudamqp.com'}
    r = requests.get(url + '/api/whoami')
    print(url, r.status_code)

file = open('test.txt', 'r')
for url in file:
    url = url.rstrip('\n');
    get_status(url)
