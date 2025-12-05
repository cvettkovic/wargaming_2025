import sqlite3 as sql


def create_connection_and_cursor(db_name):
    connection = sql.connect(db_name)
    cursor = connection.cursor()

    return (connection, cursor)


def create_ships_table(connection, cursor):
    sql_command = """
        CREATE TABLE IF NOT EXISTS ships (
            ship TEXT PRIMARY KEY,
            weapon TEXT NOT NULL,
            hull TEXT NOT NULL,
            engine TEXT NOT NULL
        )
        """
    cursor.execute(sql_command)
    connection.commit()


def create_weapons_table(connection, cursor):
    sql_command = """
        CREATE TABLE IF NOT EXISTS weapons (
            weapon TEXT PRIMARY KEY,
            reload_speed INT NOT NULL,
            rotational_speed INT NOT NULL,
            diameter INT NOT NULL,
            power_volley INT NOT NULL,
            count INT NOT NULL,
            FOREIGN KEY (weapon) REFERENCES ships(weapon)
        )
        """
    cursor.execute(sql_command)
    connection.commit()


def create_hulls_table(connection, cursor):
    sql_command = """
        CREATE TABLE IF NOT EXISTS hulls (
            hull TEXT PRIMARY KEY,
            armor INT NOT NULL,
            type INT NOT NULL,
            capacity INT NOT NULL,
            FOREIGN KEY (hull) REFERENCES ships(hull)
        )
        """
    cursor.execute(sql_command)
    connection.commit()


def create_engines_table(connection, cursor):
    sql_command = """
        CREATE TABLE IF NOT EXISTS engines (
            engine TEXT PRIMARY KEY,
            power INT NOT NULL,
            type INT NOT NULL,
            FOREIGN KEY (engine) REFERENCES ships(engine)
        )
        """
    cursor.execute(sql_command)
    connection.commit()


DB_NAME = "wargaming_task_db.db"

connection, cursor = create_connection_and_cursor(DB_NAME)

create_ships_table(connection, cursor)
create_engines_table(connection, cursor)
create_hulls_table(connection, cursor)
create_weapons_table(connection, cursor)

connection.close()

