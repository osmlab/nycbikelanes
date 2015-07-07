# Find the MapRoulette tasks for a given challenge with a status

import click
import json
import requests


def get_by_status(host, port, challenge_id, status):
    url = 'http://%s:%s/api/admin/challenge/%s/tasks' % (
        host,
        port,
        challenge_id,
    )
    response = requests.get(url)
    for task in response.json():
        if task['status'] == status:
            yield task


@click.command()
@click.option('--host', default='maproulette.org')
@click.option('--port', default='80')
@click.option('--challenge-id')
@click.option('--status')
def maproulette_by_status(host, port, challenge_id, status):
    print json.dumps(list(get_by_status(host, port, challenge_id, status)))

if __name__ == '__main__':
    maproulette_by_status()
