import csv
import os
import psycopg2 as ps
import logging
import pandas as pd

connection = ps.connect(os.environ.get('DATABASE_URL'), sslmode='require')
cursor = connection.cursor()
logging.basicConfig(level=logging.ERROR)


def get_subscriptions(status=True):
    """Get all active subscribers to the bot"""
    with connection:
        cursor.execute("SELECT * FROM subscriptions WHERE status = %s", (status,))
        return cursor.fetchall()


def get_new_properties():
    with connection:
        cursor.execute("SELECT * FROM uploadedproperties")
        return cursor.fetchall()


def get_column_names():
    with connection:
        cursor.execute("SELECT * FROM uploadedproperties")
        col_names = [desc[0] for desc in cursor.description]
        return col_names


def subscriber_exists(user_id):
    """Check if there already is such a subscriber in the database"""
    with connection:
        cursor.execute('SELECT * FROM subscriptions WHERE user_id = %s', (user_id,))
        return bool(len(cursor.fetchall()))


def add_subscriber(user_id, status=True):
    """Add a new subscriber"""
    with connection:
        return cursor.execute("INSERT INTO subscriptions (user_id, status) VALUES(%s, %s)",
                                   (user_id, status))



def update_subscription(user_id, status):
    """Change status of the subscriber"""
    with connection:
        return cursor.execute("UPDATE subscriptions SET status = %s WHERE user_id = %s", (status, user_id))


def create_table(tableName, colString):
    with connection:
        logging.critical(f'Table name: {tableName}; \n Column string: {colString}')
        cursor.execute("DROP TABLE IF EXISTS %s;" % (tableName,))
        create_table_query = "CREATE TABLE %s (%s);" % (tableName, colString)
        logging.critical(create_table_query)
        cursor.execute(create_table_query)
        # cursor.execute(f"ALTER TABLE {tableName} ADD PRIMARY KEY (link);")
        connection.commit()


# def uploadCSV(file, tableName):
#     SQL_STATEMENT = """
#             COPY %s FROM STDIN WITH
#                 CSV
#                 HEADER
#                 DELIMITER AS ','
#             """
#     cursor.copy_expert(sql=SQL_STATEMENT % tableName, file=file)
#     cursor.execute("grant select on table %s to public" % tableName)
#     connection.commit()


def uploadCSV(df, tableName):
    for _, row in df.iterrows():
        query = cursor.mogrify(f"INSERT INTO {tableName} "
                       f"({', '.join(df.columns)}) "
                       f"VALUES ({', '.join([__surround_string(str(val)) for val in row])})")
        logging.critical(query)
        cursor.execute(query)
    connection.commit()


def __surround_string(string):
    return "'" + string + "'"


def close():
    """Close database"""
    cursor.close()
    connection.close()
