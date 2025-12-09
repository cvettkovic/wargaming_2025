import utils.random_utils as rand


def get_all_from_table(connection, table_name):
    cursor = connection.cursor()

    select_sql_command = """
            SELECT *
            FROM ?
            """
    cursor.execute(select_sql_command, table_name)
    connection.commit()

    return cursor.fetchall()


def get_from_table(connection, table_name, key_name, key_value):
    cursor = connection.cursor()

    select_sql_command = """
            SELECT *
            FROM ?
            WHERE ? = ?
            """
    cursor.execute(select_sql_command, (table_name, key_name, key_value))
    cursor.commit()

    return cursor.fetchall()


def alter_all_weapons(connection):
    all_weapons = get_all_from_table(connection, "weapons")
    all_weapons = [rand.change_random_integer_and_move_first_element(weapon)
                   for weapon
                   in all_weapons]
    
    update_sql_command = """
            UPDATE weapons
            SET reload_speed = ?,
                rotational_speed = ?,
                diameter = ?,
                power_volley = ?,
                count = ?
            WHERE weapon = ?
            """
    connection.cursor().executemany(update_sql_command, all_weapons)
    connection.commit()


def alter_all_hulls(connection):
    all_hulls = get_all_from_table(connection, "hulls")
    all_hulls = [rand.change_random_integer_and_move_first_element(hull)
                 for hull
                 in all_hulls]
    
    update_sql_command = """
            UPDATE hulls
            SET armor = ?,
                type = ?,
                capacity = ?
            WHERE hull = ?
            """
    connection.cursor().executemany(update_sql_command, all_hulls)
    connection.commit()


def alter_all_engines(connection):
    all_engines = get_all_from_table(connection, "engines")
    all_engines = [rand.change_random_integer_and_move_first_element(engine)
                   for engine
                   in all_engines]
    
    update_sql_command = """
            UPDATE engines
            SET power = ?,
                type = ?
            WHERE engine = ?
            """
    connection.cursor().executemany(update_sql_command, all_engines)
    connection.commit()

