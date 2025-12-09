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
    if "ships_data" in metafunc.fixturenames:
        connection = sql.connect(constants.DB_NAME)
        ships_data = db.get_all_from_table(connection, "ships")
        metafunc.parametrize("ships_data", ships_data)

