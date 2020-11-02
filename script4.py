# Script 4 - NSSA 221 - Sam Benoist


from geolite2 import geolite2
import sys
import re
import csv


# parses IP addresses from syslog file
def parse():
    filename = sys.argv[1]
    try:
        with open(filename) as fp:
            raw_ip = []
            ip_count = []
            sorted_count = []

            string = fp.readlines()
            # regex cmd to extract IP addr
            pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

            # adds all ip addresses to lst: raw_ip
            for line in string:
                x = pattern.search(line)
                if x is None:
                    pass
                else:
                    raw_ip.append(x.group())

            # iterate over raw_ip's and add to dictionary w/ count
            ip_and_count = dict()
            for item in set(raw_ip):
                if raw_ip.count(item) >= 10:
                    ip_count.append(raw_ip.count(item))
                    ip_and_count[item] = raw_ip.count(item)

            # ordered ip_count
            sorted_count = sorted(ip_count, reverse=True)

            status_report = csv.writer(open("status_report.csv", "w"))
            for val in sorted_count:
                for key, value in ip_and_count.items():
                    if val == value:
                        reader = geolite2.reader()
                        # match = reader.get(item)['country']['names']['en']
                        status_report.writerow([val, key, reader.get(key)['country']['names']['en']])
    except IOError:
        print('File not found')


parse()
