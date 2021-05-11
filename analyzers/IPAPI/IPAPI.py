#!/usr/bin/env python
import requests
from cortexutils.analyzer import Analyzer


class IPAPI(Analyzer):

    def __init__(self):
        Analyzer.__init__(self)
        self.test_key = self.get_param('config.key', None, 'Missing IPAPI API key')

    def summary(self, raw):
        taxonomies = []
        level = 'info'
        namespace = 'IPAPI'
        predicate = 'Country'
        value = "None"
        if "country_code" in raw:
            value = "{}".format(raw["country_code"])
        taxonomies.append(self.build_taxonomy(level, namespace, predicate, value))
        return {'taxonomies': taxonomies}

    def run(self):
        Analyzer.run(self)
        if self.data_type == 'ip':
            try:
                data = self.get_data()
                s = requests.Session()
                response_details = s.get("http://api.ipapi.com/{}?access_key={}".format(data, self.test_key))
                if response_details.status_code == 200:
                    result = response_details.json()
                    self.report(result if len(result) > 0 else {})
                else:
                    self.error('Failed to query IPAPI details. Status_code {}'.format(response_details.status_code))
            except Exception as e:
                self.unexpectedError(e)
        else:
            self.notSupported()


if __name__ == '__main__':
    IPAPI().run()
