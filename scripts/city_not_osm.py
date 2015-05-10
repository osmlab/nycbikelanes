"""
Provide instructions for adding a bike lane given its properties.
"""
def instruction(properties):
    return "Add this class %s bike lane on %s. The city's data says it is %s." % (
        properties['facilitycl'],
        properties['street_1'],
        get_facility(properties).lower(),
    )


def get_facility(properties):
    return '/'.join(list(set(filter(None, [properties['ft_facilit'],
                                           properties['tf_facilit']]))))
