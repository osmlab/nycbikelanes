# Find the tasks in the original GeoJSON file

import click
import geojson
import json


def get_matching(features, segmentids):
    return filter(lambda f: f['properties']['segmentid'] in segmentids, features)


@click.command()
@click.argument('geojson-file')
@click.argument('tasks-file')
def tasks_from_geojson(geojson_file, tasks_file):
    features = geojson.load(open(geojson_file, 'r'))['features']
    tasks = json.load(open(tasks_file, 'r'))
    segmentids = [t['identifier'].split('-')[2] for t in tasks]
    print geojson.dumps(geojson.FeatureCollection(get_matching(features, segmentids)))


if __name__ == '__main__':
    tasks_from_geojson()
