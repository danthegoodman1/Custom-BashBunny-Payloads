#!/usr/bin/env python

import os
import re
import argparse

# Arguments

# demoEx = re.compile("^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$")
googleEX = re.compile("Austin|Castellano")
from os.path import expanduser

homeDir = expanduser("~")

fileList = ['.txt', '.docx', '.abcdp']

foundList = []

def searchThroughFolder(folder, expression, filetypes):
    """
    Documentation
    """
    for root, dirs, files in os.walk(folder):
        for file in files:
            for f in filetypes:
                if file.endswith(f):
                    fileLocation = os.path.join(root, file)
                    print("Checking file: " + fileLocation)
                    searchThroughFile(fileLocation, expression)

def searchThroughFile(filename, expression):
    for i, line in enumerate(open(filename)):
        for match in re.finditer(expression, line):
            found = 'Found in file: "{2}" on line {0}: {1}'.format(i+1, match.groups(), filename)
            print found
            foundList.append(found)

if __name__ == "__main__":
    searchThroughFolder(homeDir + "/Library/Application Support/AddressBook/Metadata", googleEX, fileList)
    print foundList
