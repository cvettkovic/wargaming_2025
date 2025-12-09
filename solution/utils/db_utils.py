import utils.random_utils as rand


def get_from_table(connection, table_name, columns=None):
    cursor = connection.cursor()

    select_sql_command = f"""
            SELECT {"*" if columns is None else columns}
            FROM {table_name}
            """
    cursor.execute(select_sql_command)
    connection.commit()

    return cursor.fetchall()


def get_single_from_table(connection, table_name, key_name, key_value):
    cursor = connection.cursor()

    select_sql_command = f"""
            SELECT *
            FROM {table_name}
            WHERE {key_name} = ?
            """
    cursor.execute(select_sql_command, (key_value,))
    connection.commit()

    return cursor.fetchone()


def alter_all_weapons(connection):
    all_weapons = get_from_table(connection, "weapons")
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
    all_hulls = get_from_table(connection, "hulls")
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
    all_engines = get_from_table(connection, "engines")
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

