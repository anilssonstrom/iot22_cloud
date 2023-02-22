import os
import sqlite3
from sqlite3 import Error


def create_connection(path: str):
    """Open path as a database"""
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error {e} occured")
    return connection


def execute_query(connection, query: str):
    """Use this function when making changes to the data"""

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query: str, limit: int = None):
    """Use this function to read data from database"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        if limit is None:
            result = cursor.fetchall()
        else:
            result = cursor.fetchmany(limit)
        return result
    except Error as e:
        print(f"The error {e} occured")


def main():
    current_folder = os.path.abspath(os.path.dirname(__file__))
    dbfile_path = os.path.join(current_folder, "movies.db")
    # "D:\Dev\ito22_cloud\Lectures\Lecture 8\movies.db"
    connection = create_connection(dbfile_path)

    # Example of a SQL query
    query = """
    SELECT movies.title, movies.vote_average, directors.name
    FROM movies
    INNER JOIN directors on movies.director_id = directors.id
    WHERE directors.name = "Tony Scott"
    ORDER BY movies.vote_average DESC;
    """

    answer = execute_read_query(connection, query, limit=5)

    for i, row in enumerate(answer):
        print(f"{i+1}: {row}")


if __name__ == '__main__':
    main()
