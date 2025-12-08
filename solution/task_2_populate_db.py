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
    sql_command = """
        INSERT INTO ships (ship, weapon, hull, engine)
        VALUES (?, ?, ?, ?)
        """
    ship_name_template = "Ship-{ship_number}"
    sql_command_parameters = []

    for i in range(1, constants.NUMBER_OF_SHIPS_IN_DB + 1):
        final_ship_name = ship_name_template.format(ship_number = i)
        chosen_weapon = random.choice(weapons)
        chosen_hull = random.choice(hulls)
        chosen_engine = random.choice(engines)

        sql_command_parameters.append((final_ship_name,
                                      chosen_weapon,
                                      chosen_hull,
                                      chosen_engine,
                                      ))

    cursor.executemany(sql_command, sql_command_parameters)
    connection.commit()


def populate_weapons_table(connection, cursor):
    sql_command = """
        INSERT INTO weapons (weapon, reload_speed, rotational_speed,
                            diameter, power_volley, count)
        VALUES (?, ?, ?, ?, ?, ?)
        """
    weapon_name_template = "Weapon-{weapon_number}"
    weapons_list = []
    sql_command_parameters = []

    for i in range(1, constants.NUMBER_OF_WEAPONS_IN_DB + 1):
        final_weapon_name = weapon_name_template.format(weapon_number = i)

        sql_command_parameters.append((final_weapon_name,
                                       get_random_number(),
                                       get_random_number(),
                                       get_random_number(),
                                       get_random_number(),
                                       get_random_number(),
                                       ))
        weapons_list.append(final_weapon_name)
    
    cursor.executemany(sql_command, sql_command_parameters)
    connection.commit()

    return weapons_list


def populate_hulls_table(connection, cursor):
    sql_command = """
        INSERT INTO hulls (hull, armor, type, capacity)
        VALUES (?, ?, ?, ?)
        """
    hull_name_template = "Hull-{hull_number}"
    hulls_list = []
    sql_command_parameters = []

    for i in range(1, constants.NUMBER_OF_HULLS_IN_DB + 1):
        final_hull_name = hull_name_template.format(hull_number = i)
        
        sql_command_parameters.append((final_hull_name,
                                       get_random_number(),
                                       get_random_number(),
                                       get_random_number(),
                                       ))
        hulls_list.append(final_hull_name)
    
    cursor.executemany(sql_command, sql_command_parameters)
    connection.commit()

    return hulls_list


def populate_engines_table(connection, cursor):
    sql_command = """
        INSERT INTO engines (engine, power, type)
        VALUES (?, ?, ?)
        """
    engine_name_template = "Engine-{engine_number}"
    engines_list = []
    sql_command_parameters = []

    for i in range(1, constants.NUMBER_OF_ENGINES_IN_DB + 1):
        final_engine_name = engine_name_template.format(engine_number = i)
        
        sql_command_parameters.append((final_engine_name,
                                       get_random_number(),
                                       get_random_number(),
                                       ))
        engines_list.append(final_engine_name)
    
    cursor.executemany(sql_command, sql_command_parameters)
    connection.commit()

    return engines_list


connection, cursor = create_connection_and_cursor(constants.DB_NAME)

weapons = populate_weapons_table(connection, cursor)
hulls = populate_hulls_table(connection, cursor)
engines = populate_engines_table(connection, cursor)
populate_ships_table(connection, cursor, weapons, hulls, engines)

connection.close()

