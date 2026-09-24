#Day 3 Interview preparation
#Topics modules,packages, pips
#Checking if the configuration file exists or not
import os
from zipfile import Path

config_file = "config.json"

if os.path.exists(config_file):
    print("Configuration found")
else:
    print("Configuration missing")

import os

print(os.getcwd())

for file in Path(".").iterdir():
    print(file)
