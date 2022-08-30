# import sqlite3
import psycopg2
from psycopg2 import Error


def runQuery(query_str,query_type):
    result = []
    try:
        connection = psycopg2.connect(
            user="lnunmydamiypgu",
            password="c15d7dfc4fa15bb17ab4411cff3adac1e012d86a4fdf2fa4e2e01d769b1c98de",
            host="ec2-35-168-122-84.compute-1.amazonaws.com",
            port="5432",
            database="d8slr01vp3bhig")
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
