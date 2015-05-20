"""
Provide instructions for adding a bike lane given its properties.
"""
def instruction(properties):
    instruction = 'Add this class %s bike lane' % properties['facilitycl']
    if properties['street_1']:
        instruction += ' on %s' % properties['street_1']
    instruction += '.'
    facility = get_facility(properties).lower()
    if facility:
        instruction += " The city's data says it is %s." % facility
    return instruction


def get_facility(properties):
    return '/'.join(list(set(filter(None, [properties['ft_facilit'],
                                           properties['tf_facilit']]))))
