import pytest
import sqlite3 as sql
import os
import utils.constants as constants
import utils.random_utils as rand


def alter_all_weapons(connection):
    cursor = connection.cursor()

    fetch_sql_command = """
            SELECT *
            FROM weapons
            """
    cursor.execute(fetch_sql_command)
    connection.commit()
    all_weapons = cursor.fetchall()

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
    cursor.executemany(update_sql_command, all_weapons)
    connection.commit()


def alter_all_hulls(connection):
    cursor = connection.cursor()

    fetch_sql_command = """
            SELECT *
            FROM hulls
            """
    cursor.execute(fetch_sql_command)
    connection.commit()
    all_hulls = cursor.fetchall()

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
    cursor.executemany(update_sql_command, all_hulls)
    connection.commit()


def alter_all_engines(connection):
    cursor = connection.cursor()

    fetch_sql_command = """
            SELECT *
            FROM engines
            """
    cursor.execute(fetch_sql_command)
    connection.commit()
    all_engines = cursor.fetchall()

    all_engines = [rand.change_random_integer_and_move_first_element(engine)
                   for engine
                   in all_engines]
    
    update_sql_command = """
            UPDATE engines
            SET power = ?,
                type = ?
            WHERE engine = ?
            """
    cursor.executemany(update_sql_command, all_engines)
    connection.commit()


#@pytest.fixture(scope="session") # FIXME
def temporary_db():
    original_db_connection = sql.connect(constants.DB_NAME)
    temporary_db_connection = sql.connect(constants.TEMPORARY_DB_NAME)

    # Copying the original DB into the temporary one
    original_db_connection.backup(temporary_db_connection)

    alter_all_engines(temporary_db_connection)
    alter_all_hulls(temporary_db_connection)
    alter_all_weapons(temporary_db_connection)

    #yield temporary_db_connection # FIXME

    original_db_connection.close()
    temporary_db_connection.close()

    # if os.path.exists(constants.TEMPORARY_DB_NAME): FIXME
    #     os.remove(constants.TEMPORARY_DB_NAME) FIXME

