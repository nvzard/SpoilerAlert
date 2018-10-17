import sqlite3

# Name of the DataBase
DATABASE_NAME = 'spoiler.db'
# Name of the Table
TABLE_NAME = 'request_records'
# Query to create a table of it already does not exists
CREATE_TABLE_QUERY = (
    'CREATE TABLE IF NOT EXISTS ' + TABLE_NAME + ' (' +
    '_id INTEGER PRIMARY KEY AUTOINCREMENT,'+
    'user_email TEXT NOT_NULL,' +
    'tv_shows BLOB,' +
    'date_time TEXT);'
)
# Query to insert data into the table(email, tv_show_list, timestamp)
INSERT_DATA_QUERY = (
    'INSERT INTO ' + TABLE_NAME + ' (user_email, tv_shows, date_time) ' +
    'VALUES ("{}", "{}", datetime("now", "localtime"));'
)


def feed_data_into_db(user_email, show_list):
    """
    Record the user interaction in the database.

    :param user_email: E-Mail address of the user
    :param show_list: List of TV Shows
    """
    # Open a connection to the SQLite database file
    # and create if it does not already exists
    conn = sqlite3.connect(DATABASE_NAME)
    # Create table if does not exist
    conn.execute(CREATE_TABLE_QUERY)
    # Convert the list of TV Shows into a string
    tv_shows_string = ', '.join(show_list)

    try:
        # Execute the query to insert data into the table
        conn.execute(INSERT_DATA_QUERY.format(user_email, show_list))
    except sqlite3.Error as err:
        print(err)
    finally:
        # Commit the transaction
        conn.commit()
        # Close the connection to the SQLite database
        conn.close()
    # Inform user that the interaction has been recorded
    print('\n**Database Entry Successful**\n')
