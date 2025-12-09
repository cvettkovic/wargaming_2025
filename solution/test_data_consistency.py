import utils.db_utils as db
import utils.diff_utils as diff


def test_ship_weapon_differences(ship_weapon_data, db_connections):
    original_db_connection, temporary_db_connection = db_connections
    ship, weapon = ship_weapon_data
    diffs = []

    original_weapon = db.get_single_from_table(original_db_connection,
                                        "weapons",
                                        "weapon",
                                        weapon)
    altered_weapon = db.get_single_from_table(temporary_db_connection,
                                        "weapons",
                                        "weapon",
                                        weapon)
    diffs.extend(diff.check_weapons_diff(ship,
                                         original_weapon,
                                         altered_weapon))

    assert not diffs, "; ".join(diffs)


def test_ship_hull_differences(ship_hull_data, db_connections):
    original_db_connection, temporary_db_connection = db_connections
    ship, hull = ship_hull_data
    diffs = []

    original_hull = db.get_single_from_table(original_db_connection,
                                        "hulls",
                                        "hull",
                                        hull)
    altered_hull = db.get_single_from_table(temporary_db_connection,
                                        "hulls",
                                        "hull",
                                        hull)
    diffs.extend(diff.check_hulls_diff(ship,
                                       original_hull,
                                       altered_hull))

    assert not diffs, "; ".join(diffs)


def test_ship_engine_differences(ship_engine_data, db_connections):
    original_db_connection, temporary_db_connection = db_connections
    ship, engine = ship_engine_data
    diffs = []

    original_engine = db.get_single_from_table(original_db_connection,
                                        "engines",
                                        "engine",
                                        engine)
    altered_engine = db.get_single_from_table(temporary_db_connection,
                                        "engines",
                                        "engine",
                                        engine)
    diffs.extend(diff.check_engines_diff(ship,
                                         original_engine,
                                         altered_engine))

    assert not diffs, "; ".join(diffs)

