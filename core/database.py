import sqlite3


DATABASE_NAME = 'spoiler.db'
TABLE_NAME = 'request_records'

CREATE_TABLE_QUERY = (
	'CREATE TABLE IF NOT EXISTS ' + TABLE_NAME + ' (' +
    '_id INTEGER PRIMARY KEY AUTOINCREMENT,'+
    'user_email TEXT NOT_NULL,' +
    'tv_shows BLOB,' +
    'date_time TEXT);'
)

INSERT_DATA_QUERY = (
	'INSERT INTO ' + TABLE_NAME + ' (user_email, tv_shows, date_time) ' +
	'VALUES ("{}", "{}", datetime("now", "localtime"));'
)


def feed_data_into_db(user_email, show_list):
	conn = sqlite3.connect(DATABASE_NAME)

	# Create table if does not exist
	conn.execute(CREATE_TABLE_QUERY)

	# Convert the list of TV Shows into a string
	tv_shows_string = ', '.join(show_list)

	try:
		conn.execute(INSERT_DATA_QUERY.format(user_email, show_list))
	except sqlite3.Error as err:
		print(err)
	finally:
		conn.commit()
		conn.close()

	print('\n**Database Entry Successful**\n')