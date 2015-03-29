import argparse
import geojson
import json
import sys


def null_instruction(properties):
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=('GeoJSON file to JSON file that is suitable for '
                     'importing into MapRoulette using maproulette-loader')
    )
    parser.add_argument('--instruction_module',
        dest='instruction_module',
        help='A python module that returns instructions for a task',
    )
    args = parser.parse_args()

    input_geojson = geojson.load(sys.stdin)
    output_json = sys.stdout
    try:
        instruction_function = __import__(args.instruction_module).instruction
    except Exception:
        instruction_function = null_instruction


    tasks = []
    for feature in input_geojson['features']:
        tasks.append({
            'geometries': geojson.FeatureCollection([feature,]),
            'instruction': instruction_function(feature['properties']),
        })
    json.dump(tasks, output_json)
