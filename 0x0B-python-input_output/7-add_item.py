#!/usr/bin/python3
"""
    This script is used to add all arguments used earlier.
"""
import sys
arguments = sys.argv[1:]
save_to_json_file = __import__(
    "5-save_to_json_file").save_to_json_file(arguments, "add_item.json")

load_from_json_file = __import__(
    "6-load_from_json_file").load_from_json_file("add_item.json")
