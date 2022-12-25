import time
import requests
import json

from typing import Iterator

from settings import log_filename, export_api_path


def follow(file, sleep_sec=1) -> Iterator[str]:
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
    if 'auditID' in entry:
        audit_id = entry['auditID']
        print(f"Exporting audit_item with id '{audit_id}'")
    requests.put(
            export_api_path, 
            data=json.dumps(entry, ensure_ascii=False)
        )


def main():
    print("Exporter started")
    print(f"Watching audit_log file at '{log_filename}'")
    idle = True
    while idle:
        try:
            with open(log_filename, 'r') as file:
                for line in follow(file):
                    parsed = parse_log_entry(line)
                    report_log_entry(parsed)
        except Exception as e:
            print(f"Exception occured: {e}")
            idle = False


if __name__ == "__main__":
    main()
