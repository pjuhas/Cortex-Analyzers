#!/usr/bin/env python3
import json
from cortexutils.analyzer import Analyzer


class KapeJSONParser(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)
        self.filename = self.getParam('attachment.name', 'noname.ext')
        self.filepath = self.getParam('file', None, 'File is missing')

    def run(self):
        if self.data_type == 'file':
            try:
                with open(self.filepath, 'r', encoding='utf-16') as file:
                    data = json.load(file)

                values = [{key: value for key, value in _.items() if
                           key in ["Name", "ProcessID", "Path", "commandline", "Owner", "Parent Path",
                                   "ParentProcessId"]} for _ in
                          data]
                result = {"data": values}
                self.report(result if len(result) > 0 else {})
            except Exception as e:
                self.unexpectedError(e)
        else:
            self.notSupported()

    def summary(self, raw):
        taxonomies = []
        level = "info"
        namespace = "KapeJSONParser"
        predicate = ""
        value = "Success"
        taxonomies.append(self.build_taxonomy(level, namespace, predicate, value))
        return {"taxonomies": taxonomies}


if __name__ == '__main__':
    KapeJSONParser().run()
