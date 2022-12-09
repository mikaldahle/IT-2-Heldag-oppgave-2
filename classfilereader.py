# Nicolai

import json
import csv
import os
import chardet
import pprint
from pathlib import Path

fileTypes = ['json','csv']


def get_delimiter(path):
    with open(path, 'r') as file:
        sniffer = csv.Sniffer()
        sniffer.preferred = [';', ',', '\t', ':']
        return str(sniffer.sniff(file.read()).delimiter)


def get_encoding(path, n_lines=20):
    with Path(path).open('rb') as f:
        rawdata = b''.join([f.readline() for _ in range(n_lines)])
        return chardet.detect(rawdata)['encoding']

class read():
    def __init__(self, filename, delimeter=None, format='None'):
        self.name = filename
        self.type = filename.split(".",1)[1]

        self.content = []
        self.rows = []
        self.delimiter = get_delimiter(
            filename) if delimeter == None else delimeter
        self.encode = get_encoding(filename)
        self.format = format
        self.headlines = None
        self.path = Path(__file__).parent/filename

        print("Reading {}".format(self.name))

        if self.type == "csv":
            with open(filename, encoding=self.encode) as fil:
                content = csv.reader(fil, delimiter=self.delimiter) if not format == 'dict' else csv.DictReader(
                    fil, delimiter=self.delimiter)
                self.headlines = next(
                    content) if not format == 'dict' else None
                self.content = [[v for v in rad] for rad in content] if not format == 'dict' else [
                    v for v in content]
        else:
            with open(filename, encoding=self.encode) as fil:
                fil = json.load(fil)
                self.content.append(fil)

                #pp = pprint.PrettyPrinter(indent=4, width=80, compact=True)

                #print("Pretty Printing JSON Data using pprint module")
                #pp.pprint(fil)



def main():
    avaliable = [i for i in os.listdir() if i.split('.')[len(i.split('.'))-1] in fileTypes]
    return [read(v) for v in avaliable]
