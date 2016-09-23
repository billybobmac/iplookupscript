#!/usr/bin/python
# -*- coding: utf-8 -*-
# For rollout need store network addresses.
# Have list of stores, and hostnames.
# Take CSV of hostnames in stores.csv, and adds column of IP address in file result.csv.
# This script does no sanitizing of the input stores.csv file!

# Example stores.csv
# store1000
# store1001
# store1002
# store1003

# Example result.csv
# store1000,10.0.0.1
# store1001,10.0.1.1
# store1002,10.0.2.1
# store1003,10.0.3.1

# CSV library from Python

import csv

# Socket library adds ability to lookup IPs.

import socket

# Opens the file

with open('stores.csv', 'rb') as f:
    csvfile = csv.reader(f)

    # results list.

    result = []

    # Row by row of the file.

    for row in csvfile:

        # Gets hostname out of CSV file.

        hostname = row[0]

        # Gets ip address

        ipaddress = socket.gethostbyname(hostname)

        # Adds ip address to row list

        row.append(ipaddress)

        # Adds row with newly added IP address to result list.

        result.append(row)

# Opens results.csv file for writing.

with open('results.csv', 'wb') as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)

    # Writes each row in file.

    for row in result:
        wr.writerow(row)


			