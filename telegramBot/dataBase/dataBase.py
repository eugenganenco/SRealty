import csv
import os
import psycopg2 as ps
import logging

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
    logging.critical(f'Table name: {tableName}; \n Column string: {colString}')
    cursor.execute("DROP TABLE IF EXISTS %s;" % (tableName,))
    cursor.execute("CREATE TABLE %s (%s);" % (tableName, colString))
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

def uploadCSV(file, tableName, colString):
    # create table
    logging.critical(f'Table name: {tableName}; \n Column string: {colString}')
    cursor.execute("DROP TABLE IF EXISTS %s;" % (tableName,))
    cursor.execute("CREATE TABLE %s (%s);" % (tableName, colString))

    # read the contents of the file
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        rows = [row for row in reader]

    # populate the table
    insert_query = f"INSERT INTO {tableName} (name, age, city) VALUES %s"
    connection.execute_values(cursor, insert_query, rows)

def close():
    """Close database"""
    cursor.close()
    connection.close()
