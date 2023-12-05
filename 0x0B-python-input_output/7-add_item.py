#!/usr/bin/python3
"""a script that adds all arguments to a
python list and saves them to a file.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_json_list = []
try:
    my_json_list = load_from_json_file(filename)
except Exception as e:
    pass

my_json_list += sys.argv[1:]
save_to_json_file(my_json_list, filename)
