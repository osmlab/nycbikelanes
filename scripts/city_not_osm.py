"""
Provide instructions for adding a bike lane given its properties.
"""


facility_translations = {
    'bridge': 'on a bridge',
    'dirt trail': 'part of a dirt trail',
    'greenway': 'part of a greenway',
    'protected path': 'part of a protected path',
    'signed route': 'part of a signed route',
    'standard': 'part of a standard bike lane',
}

directions_url = 'https://github.com/osmlab/nycbikelanes/blob/master/challenges/city_not_osm/directions.md'


def instruction(properties):
    instruction = 'Add this class %s bike lane' % properties['facilitycl']
    if properties['street']:
        instruction += ' on %s' % properties['street']
    instruction += '.'
    facility = get_facility(properties).lower()
    if facility:
        instruction += " The city's data says it is %s.\n\n" % facility
    instruction += '**[View more detailed directions](%s)**' % directions_url
    return instruction


def get_facility(properties):
    facilities = list(set(filter(None, [properties['ft_facilit'], properties['tf_facilit']])))
    facilities = map(lambda f: facility_translations.get(f.lower(), f), facilities)
    return '/'.join(facilities)
