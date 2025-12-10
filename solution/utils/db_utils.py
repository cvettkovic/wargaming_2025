import utils.random_utils as rand


def get_from_table(connection, table_name, columns=None):
    """
    Return a list of tuples from the table.
    This function is not safe and can be exploited.

    :param connection: Connection to the database.
    :param table_name: Table to fetch data from.
    :param columns: Columns to fetch (default: all columns).
    """
    cursor = connection.cursor()

    # Exploit: SQL injection, but sufficient enough for this task's needs
    select_sql_command = f"""
            SELECT {"*" if columns is None else columns}
            FROM {table_name}
            """
    cursor.execute(select_sql_command)

    return cursor.fetchall()


def get_single_from_table(connection, table_name, key_name, key_value):
    """
    Return a single tuple from the table.
    This function is not safe and can be exploited.

    :param connection: Connection to the database.
    :param table_name: Table to fetch data from.
    :param key_name: Name of the column to compare the values from.
    :param key_value: Value to compare to.
    """
    cursor = connection.cursor()

    # Exploit: SQL injection, but sufficient enough for this task's needs
    select_sql_command = f"""
            SELECT *
            FROM {table_name}
            WHERE {key_name} = ?
            """
    cursor.execute(select_sql_command, (key_value,))

    return cursor.fetchone()


def alter_all_weapons(connection):
    """
    Alter a random non-key column in 'weapons' table to a random value.
    
    :param connection: Connection to the database.
    """
    all_weapons = get_from_table(connection, "weapons")
    # Prepare and format data for updating
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
    """
    Alter a random non-key column in 'hulls' table to a random value.
    
    :param connection: Connection to the database.
    """
    all_hulls = get_from_table(connection, "hulls")
    # Prepare and format data for updating
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
    """
    Alter a random non-key column in 'engines' table to a random value.
    
    :param connection: Connection to the database.
    """
    all_engines = get_from_table(connection, "engines")
    # Prepare and format data for updating
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

