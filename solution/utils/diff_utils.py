def format_diff(ship, component, parameter, expected, was):
    return f"{ship}, {component}, {parameter}: expected {expected}, was {was}"


def check_weapons_diff(ship, original_weapon, altered_weapon):
    diffs = []

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
    diffs = []

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
    diffs = []
    
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