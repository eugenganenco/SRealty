import os
import psycopg2 as ps

connection = ps.connect(os.environ.get('DATABASE_URL'), sslmode='require')
cursor = connection.cursor()


def get_subscriptions(status=True):
    """Get all active subscribers to the bot"""
    with connection:
        return cursor.execute("SELECT * FROM subscriptions WHERE status = %s", (status,)).fetchall()


def subscriber_exists(user_id):
    """Check if there already is such a subscriber in the database"""
    with connection:
        result = cursor.execute('SELECT * FROM subscriptions WHERE user_id = %s', (user_id,)).fetchall()
        return bool(len(result))


def add_subscriber(user_id, status=True):
    """Add a new subscriber"""
    with connection:
        return cursor.execute("INSERT INTO subscriptions (user_id, status) VALUES(%s, %s)",
                                   (user_id, status))


def update_subscription(user_id, status):
    """Change status of the subscriber"""
    with connection:
        return cursor.execute("UPDATE subscriptions SET status = %s WHERE user_id = %s", (status, user_id))


def close():
    """Close database"""
    cursor.close()
    connection.close()
