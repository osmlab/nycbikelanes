#!/bin/bash
DATA_FILE="challenges/city_not_osm/data.json"

source config.sh

python scripts/uploadtomaproulette.py --api-key "$API_KEY" --challenge-id $CHALLENGE_ID < $DATA_FILE
