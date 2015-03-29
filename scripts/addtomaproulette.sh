#!/bin/bash

# This is handy as a reminder of how to invoke maproulette-loader
python ../../maproulette-loader/loader.py --verbose --server localhost --port 5000 --title "Add bike lanes in NYC" --blurb "Help add bike lanes in NYC to OSM" --challenge-help "Detailed help for the bike lane challenge" --instruction "Add bike lanes that are in the city's data but not in OSM" nycbikelanes use-json test.json
