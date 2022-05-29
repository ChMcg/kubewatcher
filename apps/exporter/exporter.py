import time
import requests
import json
import os
from typing import Iterator


# log_filename = 'logs/audit-test.log'
log_filename = '/var/log/kubernetes/apiserver/audit.log'
export_path = os.getenv("EXPORT_PATH") or "http://analyzer"


def follow(file, sleep_sec=0.1) -> Iterator[str]:
    """ Yield each line from a file as they are written.
    `sleep_sec` is the time to sleep after empty reads. """
    line = ''
    while True:
        tmp = file.readline()
        if tmp is not None: 
            line += tmp
            if line.endswith("\n"):
                yield line
                line = ''
        elif sleep_sec:
            time.sleep(sleep_sec)


def parse_log_entry(entry: str) -> dict:
    return json.loads(entry.strip())

def report_log_entry(entry: dict):
    requests.put(export_path, json.dumps(entry, ensure_ascii=False))


def main():
    with open(log_filename, 'r') as file:
        for line in follow(file):
            print(line, end='')            


if __name__=="__main__":
    main()
