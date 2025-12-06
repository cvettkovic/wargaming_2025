import sqlite3 as sql
import random
import utils.constants as constants


def get_random_number(min_inclusive=constants.MIN_RANDOM_NUMBER,
                      max_inclusive=constants.MAX_RANDOM_NUMBER):
    return random.randint(min_inclusive, max_inclusive)


def create_connection_and_cursor(db_name):
    connection = sql.connect(db_name)
    cursor = connection.cursor()

    return (connection, cursor)


def populate_ships_table(connection, cursor, weapons, hulls, engines):
    sql_command_template = """
        INSERT INTO ships
        VALUES ('{ship}', '{weapon}', '{hull}', '{engine}')
        """
    ship_name_template = "Ship-{ship_number}"

    for i in range(1, constants.NUMBER_OF_SHIPS_IN_DB + 1):
        chosen_weapon = random.choice(weapons)
        chosen_hull = random.choice(hulls)
        chosen_engine = random.choice(engines)

        final_ship_name = ship_name_template.format(ship_number = i)
        final_sql_command = sql_command_template.format(
            ship = final_ship_name,
            weapon = chosen_weapon,
            hull = chosen_hull,
            engine = chosen_engine,
        )

        cursor.execute(final_sql_command)
    
    connection.commit()


def populate_weapons_table(connection, cursor):
    sql_command_template = """
        INSERT INTO weapons
        VALUES ('{weapon}', {reload_speed}, {rotational_speed},
                {diameter}, {power_volley}, {count})
        """
    weapon_name_template = "Weapon-{weapon_number}"
    weapons_list = []

    for i in range(1, constants.NUMBER_OF_WEAPONS_IN_DB + 1):
        final_weapon_name = weapon_name_template.format(weapon_number = i)
        final_sql_command = sql_command_template.format(
            weapon = final_weapon_name,
            reload_speed = get_random_number(),
            rotational_speed = get_random_number(),
            diameter = get_random_number(),
            power_volley = get_random_number(),
            count = get_random_number(),
        )

        cursor.execute(final_sql_command)
        weapons_list.append(final_weapon_name)
    
    connection.commit()

    return weapons_list


def populate_hulls_table(connection, cursor):
    sql_command_template = """
        INSERT INTO hulls
        VALUES ('{hull}', {armor}, {type}, {capacity})
        """
    hull_name_template = "Hull-{hull_number}"
    hulls_list = []

    for i in range(1, constants.NUMBER_OF_HULLS_IN_DB + 1):
        final_hull_name = hull_name_template.format(hull_number = i)
        final_sql_command = sql_command_template.format(
            hull = final_hull_name,
            armor = get_random_number(),
            type = get_random_number(),
            capacity = get_random_number(),
        )

        cursor.execute(final_sql_command)
        hulls_list.append(final_hull_name)
    
    connection.commit()

    return hulls_list


def populate_engines_table(connection, cursor):
    sql_command_template = """
        INSERT INTO engines
        VALUES ('{engine}', {power}, {type})
        """
    engine_name_template = "Engine-{engine_number}"
    engines_list = []

    for i in range(1, constants.NUMBER_OF_ENGINES_IN_DB + 1):
        final_engine_name = engine_name_template.format(engine_number = i)
        final_sql_command = sql_command_template.format(
            engine = final_engine_name,
            power = get_random_number(),
            type = get_random_number(),
        )

        cursor.execute(final_sql_command)
        engines_list.append(final_engine_name)
    
    connection.commit()

    return engines_list


connection, cursor = create_connection_and_cursor(constants.DB_NAME)

weapons = populate_weapons_table(connection, cursor)
hulls = populate_hulls_table(connection, cursor)
engines = populate_engines_table(connection, cursor)
populate_ships_table(connection, cursor, weapons, hulls, engines)

connection.close()

