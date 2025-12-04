# pyright: reportUnboundVariable=false
# pyright: reportAttributeAccessIssue=false


from mimetypes import inited
import sqlite3
from typing import List


if __name__ == "__main__":
    raise RuntimeError(f"Cannot run module {__file__}!")


_connection = None
_cursor = None
_inited = False


def _check_validity() -> None:
    if not _inited:
        raise RuntimeError(f"Must call init() first in order to use module {__file__}!")
    
    if _connection is None or _cursor is None:
        raise RuntimeError(f"Internal error in module {__file__}")


def init(db_name: str) -> None:
    if _inited:
        raise RuntimeError(f"Must call finish() first in order to call init() again!")
    
    _connection = sqlite3.connect(db_name)
    _cursor = _connection.cursor()
    _inited = True


def finish() -> None:
    _check_validity()

    _connection.close()
    _connection = None
    _cursor = None
    _inited = False


def create_table(table_name: str, list_of_columns: List[str]) -> None:
    _check_validity()

    if table_name is None or table_name == "":
        raise ValueError("Must pass proper table name!")
    if list_of_columns is None or len(list_of_columns) < 1:
        raise ValueError("Must pass at least one column!")
    
    sql_column_list = ""
    for column in list_of_columns:
        sql_column_list += f"{column},\n"
    sql_column_list = sql_column_list[:-2]

    sql_command = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                {sql_column_list}
                )
                """
    _cursor.execute(sql_command)
    _connection.commit()


def insert_into_table(table_name: str, values: tuple) -> None:
    _check_validity()

    if table_name is None or table_name == "":
        raise ValueError("Must pass proper table name!")
    if values is None or len(values) < 1:
        raise ValueError("Must pass proper number of values to insert!")
    
    sql_values_list = ""
    for value in values:
        sql_values_list += f"{value}, "
    sql_values_list = sql_values_list[:-2]
    
    sql_command = f"""
                INSERT INTO {table_name}
                VALUES ({sql_values_list})
                """
    _cursor.execute(sql_command)
    _connection.commit()


def select_from_table(table_name: str, columns: tuple = tuple(), where: str = "") -> List[tuple]:
    _check_validity()

    if table_name is None or table_name == "":
        raise ValueError("Must pass proper table name!")
    if columns is None:
        raise ValueError("Must pass valid columns parameter!")
    if where is None:
        raise ValueError("Must pass valid WHERE condition for data extraction!")
    
    if len(columns) < 1:
        sql_colums_to_get = "*"
    else:
        sql_colums_to_get = ""
        for column in columns:
            sql_colums_to_get += f"{column}, "
        sql_colums_to_get = sql_colums_to_get[:-2]
    
    if where == "":
        sql_where_statement = ""
    else:
        sql_where_statement = f"WHERE {where}"
    
    sql_command = f"""
                SELECT {sql_colums_to_get}
                FROM {table_name}
                {sql_where_statement}
                """
    _cursor.execute(sql_command)
    _connection.commit()
    
    return _cursor.fetchall()


def update_table(table_name: str, columns: tuple, values: tuple, where: str) -> None:
    _check_validity()

    if table_name is None or table_name == "":
        raise ValueError("Must pass proper table name!")
    if columns is None or len(columns) < 1:
        raise ValueError("Must pass valid columns parameter!")
    if values is None or len(values) < 1:
        raise ValueError("Must pass valid values parameter!")
    if where is None or where == "":
        raise ValueError("Must pass valid WHERE condition for data extraction!")
    if len(columns) != len(values):
        raise ValueError("Must pass same number of values for columns and values")
    
    sql_values_to_change = ""
    for i in range(0, len(columns)):
        sql_values_to_change += f"{columns[i]} = {values[i]}, "
    sql_values_to_change = sql_values_to_change[:-2]

    sql_command = f"""
                UPDATE {table_name}
                SET {sql_values_to_change}
                WHERE {where}
                """
    _cursor.execute(sql_command)
    _connection.commit()

    