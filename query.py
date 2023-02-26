# import sqlite3
import psycopg2
from psycopg2 import Error


def runQuery(query_str,query_type):
    result = []
    try:
        connection = psycopg2.connect(
            user="lfdtytgdqrhbqu",
            password="97b0e3a555d7ae30f730c48dd944cafd04f6c7338361bd86ee5d64cc17269969",
            host="ec2-54-165-184-219.compute-1.amazonaws.com",
            port="5432",
            database="dda1fmsu59fshs")
        cursor = connection.cursor()

        cursor.execute(query_str)
        if query_type == "insert":
            connection.commit()
        elif query_type == "select":
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        elif query_type == "update":
            connection.commit()
            result = cursor.rowcount

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return result
