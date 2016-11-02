import click
import json
import requests

@click.command()
@click.option('--api-key')
@click.option('--challenge-id')
@click.option('--tasks-file')
def upload(api_key, challenge_id, tasks_file):
    if tasks_file:
        tasks = json.load(open(tasks_file, 'r'))
    else:
        tasks = json.load(click.get_text_stream('stdin'))

    url = 'http://maproulette.org/api/v2/challenge/%s/tasks' % challenge_id
    headers = {
        'apiKey': api_key,
    }
    response = requests.post(url, headers=headers, json=tasks)
    print response.status_code
    print response.content

if __name__ == '__main__':
    upload()
