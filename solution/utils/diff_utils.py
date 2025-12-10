def format_diff(ship, component, parameter, expected, was):
    """
    Return formatted message for a failed test case.
    
    :param ship: Name of the ship for which the test case failed.
    :param component: Name of the component for which the test case failed.
    :param parameter: Name of the parameter for which the test case failed.
    :param expected: Value that was expected.
    :param was: Value that was encountered.
    """
    return f"{ship}, {component}, {parameter}: expected {expected}, was {was}"


def check_weapons_diff(ship, original_weapon, altered_weapon):
    """
    Check the difference between two weapons and return list of messages 
    for parameters that differ.
    
    :param ship: Name of the ship.
    :param original_weapon: Tuple for the weapon that was expected.
    :param altered_weapon: Tuple for the weapon that was encountered.
    """
    diffs = []

    # Check each parameter from two tuples
    if (original_weapon[1] != altered_weapon[1]):
        diff = format_diff(ship,
                           original_weapon[0],
                           "reload_speed",
                           original_weapon[1],
                           altered_weapon[1])
        diffs.append(diff)
    if (original_weapon[2] != altered_weapon[2]):
        diff = format_diff(ship,
                           original_weapon[0],
                           "rotational_speed",
                           original_weapon[2],
                           altered_weapon[2])
        diffs.append(diff)
    if (original_weapon[3] != altered_weapon[3]):
        diff = format_diff(ship,
                           original_weapon[0],
                           "diameter",
                           original_weapon[3],
                           altered_weapon[3])
        diffs.append(diff)
    if (original_weapon[4] != altered_weapon[4]):
        diff = format_diff(ship,
                           original_weapon[0],
                           "power_volley",
                           original_weapon[4],
                           altered_weapon[4])
        diffs.append(diff)
    if (original_weapon[5] != altered_weapon[5]):
        diff = format_diff(ship,
                           original_weapon[0],
                           "count",
                           original_weapon[5],
                           altered_weapon[5])
        diffs.append(diff)
    
    return diffs


def check_hulls_diff(ship, original_hull, altered_hull):
    """
    Check the difference between two hulls and return list of messages 
    for parameters that differ.
    
    :param ship: Name of the ship.
    :param original_hull: Tuple for the hull that was expected.
    :param altered_hull: Tuple for the hull that was encountered.
    """
    diffs = []

    # Check each parameter from two tuples
    if (original_hull[1] != altered_hull[1]):
        diff = format_diff(ship,
                           original_hull[0],
                           "armor",
                           original_hull[1],
                           altered_hull[1])
        diffs.append(diff)
    if (original_hull[2] != altered_hull[2]):
        diff = format_diff(ship,
                           original_hull[0],
                           "type",
                           original_hull[2],
                           altered_hull[2])
        diffs.append(diff)
    if (original_hull[3] != altered_hull[3]):
        diff = format_diff(ship,
                           original_hull[0],
                           "capacity",
                           original_hull[3],
                           altered_hull[3])
        diffs.append(diff)
    
    return diffs


def check_engines_diff(ship, original_engine, altered_engine):
    """
    Check the difference between two engines and return list of messages 
    for parameters that differ.
    
    :param ship: Name of the ship.
    :param original_engine: Tuple for the engine that was expected.
    :param altered_engine: Tuple for the engine that was encountered.
    """
    diffs = []
    
    # Check each parameter from two tuples
    if (original_engine[1] != altered_engine[1]):
        diff = format_diff(ship,
                           original_engine[0],
                           "power",
                           original_engine[1],
                           altered_engine[1])
        diffs.append(diff)
    if (original_engine[2] != altered_engine[2]):
        diff = format_diff(ship,
                           original_engine[0],
                           "type",
                           original_engine[2],
                           altered_engine[2])
        diffs.append(diff)
    
    return diffs

