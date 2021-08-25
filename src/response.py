#Copyright © 2021 Rauan Asetov. All rights reserved.
#License: http://opensource.org/licenses/MIT
import requests

class Request(object):
    def __init__(self, url):
        self._url = url
        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
                         'Accept': '*/*'}
        try:
            self._r = requests.get(self._url, headers=self._headers)
        except Exception as e:
            self.response = e
        else:
            self.response = self._r.status_code

    def __str__(self):
        return str(self.response)

