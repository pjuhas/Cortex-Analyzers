#!/usr/bin/env python
import requests
from cortexutils.analyzer import Analyzer


class BitcoinAbuse(Analyzer):

    def __init__(self):
        Analyzer.__init__(self)
        self.test_key = self.get_param('config.key', None, 'Missing Bitcoin Abuse API key')

    def summary(self, raw):
        taxonomies = []
        level = 'info'
        namespace = 'Bitcoin Abuse'
        predicate = 'Count'
        value = "0"
        if raw["count"] != 0:
            value = "{}".format(raw["count"])
        taxonomies.append(self.build_taxonomy(level, namespace, predicate, value))
        return {'taxonomies': taxonomies}

    def run(self):
        Analyzer.run(self)
        if self.data_type == 'string':
            try:
                data = self.get_data()
                s = requests.Session()
                response_details = s.get('https://www.bitcoinabuse.com/api/reports/check?address={}&api_token={}'
                                         .format(data, self.test_key))

                if response_details.status_code == 200 or response_details.status_code == 201:
                    result = response_details.json()
                    self.report(result if len(result) > 0 else {})
                else:
                    self.error('Failed to query Bitcoin Abuse details. Status_code {}'.format(response_details.status_code))
            except Exception as e:
                self.unexpectedError(e)
        else:
            self.notSupported()


if __name__ == '__main__':
    BitcoinAbuse().run()
