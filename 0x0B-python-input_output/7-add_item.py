#!/usr/bin/python3
"""
    This script is used to add all arguments used earlier.
"""
import sys
from os import path
arguments = sys.argv[1:]

FILENAME = "add_item.json"
# imported functions
save_to_json_file = __import__(
    "5-save_to_json_file").save_to_json_file

load_from_json_file = __import__(
    "6-load_from_json_file").load_from_json_file

# check if file exist
if path.exists(FILENAME):
    # load data from file
    data = load_from_json_file(FILENAME)
else:
    data = []

for i in arguments:
    data.append(i)
    # save data to file
    save_to_json_file(data, FILENAME)
