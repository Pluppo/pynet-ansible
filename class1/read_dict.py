#! /usr/bin/env python

filename = 'class1_dict.yml'
import yaml
from pprint import pprint

def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)

pprint(read_yaml(filename))
