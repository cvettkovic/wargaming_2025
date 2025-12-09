import pytest
import os
import utils.constants as constants
import sqlite3 as sql
import utils.db_utils as db

@pytest.fixture(scope="session")
def temporary_db():
    original_db_connection = sql.connect(constants.DB_NAME)
    temporary_db_connection = sql.connect(constants.TEMPORARY_DB_NAME)

    # Copying the original DB into the temporary one
    original_db_connection.backup(temporary_db_connection)
    original_db_connection.close()

    db.alter_all_engines(temporary_db_connection)
    db.alter_all_hulls(temporary_db_connection)
    db.alter_all_weapons(temporary_db_connection)

    yield temporary_db_connection

    temporary_db_connection.close()

    if os.path.exists(constants.TEMPORARY_DB_NAME):
        os.remove(constants.TEMPORARY_DB_NAME)


def pytest_generate_tests(metafunc):
    connection = sql.connect(constants.DB_NAME)

    if "original_weapons" in metafunc.fixturenames:
        original_weapons = db.get_all_from_table(connection, "weapons")
        metafunc.parametrize("original_weapons", original_weapons)
    elif "original_hulls" in metafunc.fixturenames:
        original_hulls = db.get_all_from_table(connection, "hulls")
        metafunc.parametrize("original_hulls", original_hulls)
    elif "original_engines" in metafunc.fixturenames:
        original_engines = db.get_all_from_table(connection, "engines")
        metafunc.parametrize("original_engines", original_engines)
    
    connection.close()


