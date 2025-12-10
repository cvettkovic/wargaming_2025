import pytest
import os
import utils.constants as constants
import sqlite3 as sql
import utils.db_utils as db


@pytest.fixture(scope="session")
def db_connections():
    original_db_connection = sql.connect(constants.DB_NAME)
    temporary_db_connection = sql.connect(constants.TEMPORARY_DB_NAME)

    # Copying the original DB into the temporary one
    original_db_connection.backup(temporary_db_connection)

    # Alter values randomly
    db.alter_all_engines(temporary_db_connection)
    db.alter_all_hulls(temporary_db_connection)
    db.alter_all_weapons(temporary_db_connection)

    yield (original_db_connection, temporary_db_connection)

    # Teardown
    original_db_connection.close()
    temporary_db_connection.close()
    if os.path.exists(constants.TEMPORARY_DB_NAME):
        os.remove(constants.TEMPORARY_DB_NAME)


def pytest_generate_tests(metafunc):
    connection = sql.connect(constants.DB_NAME)
    
    # Each test gets data from own table
    if "ship_weapon_data" in metafunc.fixturenames:
        ship_weapon_data = db.get_from_table(connection,
                                             "ships",
                                             columns="ship, weapon")
        metafunc.parametrize("ship_weapon_data", ship_weapon_data)
    elif "ship_hull_data" in metafunc.fixturenames:
        ship_hull_data = db.get_from_table(connection,
                                             "ships",
                                             columns="ship, hull")
        metafunc.parametrize("ship_hull_data", ship_hull_data)
    elif "ship_engine_data" in metafunc.fixturenames:
        ship_engine_data = db.get_from_table(connection,
                                             "ships",
                                             columns="ship, engine")
        metafunc.parametrize("ship_engine_data", ship_engine_data)
    
    connection.close()

