#!/usr/bin/env python
import requests
from cortexutils.analyzer import Analyzer


class W3SA(Analyzer):

    def __init__(self):
        Analyzer.__init__(self)
        self.admin = self.get_param('config.login', None, 'Missing login for W3SA-UPJS')
        self.passwd = self.get_param('config.password', None, 'Missing password for W3SA-UPJS')

    def summary(self, raw):
        taxonomies = []
        level = 'malicious'
        namespace = 'W3SA'
        predicate = 'IP'
        value = "False"
        if len(raw["table"]) != 0:
            value = "True"
            level = "safe"
        taxonomies.append(self.build_taxonomy(level, namespace, predicate, value))
        return {'taxonomies': taxonomies}

    def run(self):
        Analyzer.run(self)
        if self.data_type == 'ip':
            try:
                data = self.get_data()
                payload = {
                    'login': self.admin,
                    'password': self.passwd,
                }

                with requests.Session() as s:
                    s.post('https://w3sa.ciakt.upjs.sk/login_handler?came_from=%2Fadmin%2F&amp;__logins=0',
                               data=payload)
                    r = s.get('https://w3sa.ciakt.upjs.sk/admin/services/export_all_devices.json?ip={}'.format(
                        data))
                if r.status_code == 200:
                    result = r.json()
                    self.report(result if len(result) > 0 else {})
                else:
                    self.error(
                        'Failed to connect to W3SA-UPJS. Status_code {}'.format(r.status_code))
            except Exception as e:
                self.unexpectedError(e)
        else:
            self.notSupported()


if __name__ == '__main__':
    W3SA().run()
