#!/usr/bin/env python3
from cortexutils.analyzer import Analyzer
import iocextract


class KapeIPParser(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)

        # filename of the observable
        self.filename = self.getParam('attachment.name', 'noname.ext')

        # filepath to the observable, looks like /tmp/cortex-4224850437865873235-datafile
        self.filepath = self.getParam('file', None, 'File is missing')

    def run(self):
        if self.data_type == 'file':
            try:
                address = []
                with open(self.filepath, 'r', encoding='utf-16') as file:
                    for line in file:
                        x = line.split()
                        if "ESTABLISHED" in x:
                            address.append(x[2].split(":")[0])
                file.close()
                address = list(set(address))
                result = {"count": len(address), "address": []}
                for x in address:
                    result["address"].append({"IP": x})
                self.report(result if len(result) > 0 else {})
            except Exception as e:
                self.unexpectedError(e)
        else:
            self.notSupported()

    def summary(self, raw):
        taxonomies = []
        level = "info"
        namespace = "KapeIPParser"
        predicate = "Different IPs"
        value = "0"
        if raw["count"] != 0:
            value = "{}".format(raw["count"])

        taxonomies.append(self.build_taxonomy(level, namespace, predicate, value))
        return {"taxonomies": taxonomies}

    def artifacts(self, raw):
        artifacts = []
        ipv4s = list(iocextract.extract_ipv4s(str(raw)))
        if ipv4s:
            for i in ipv4s:
                artifacts.append(self.build_artifact('ip', str(i)))
        return artifacts


if __name__ == '__main__':
    KapeIPParser().run()
