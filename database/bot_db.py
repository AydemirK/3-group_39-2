import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_table(self):
        if self.connection:
            print('connecting to database successfully!')

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_DISLIKE_TABLE_QUERY)

        self.connection.commit()

    def sql_insert_all_users(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY, (None, telegram_id, username, first_name, last_name)
        )
        self.connection.commit()

    def select_ban_user(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'count': row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY, (telegram_id,)
        ).fetchone()

    def insert_ban_user(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY, (None, telegram_id, 1)
        )
        self.connection.commit()

    def update_ban_user(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_COUNT, (telegram_id,)
        )
        self.connection.commit()

    def ban_user(self, telegram_id):
        self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY, (telegram_id,)
        )

    def insert_profile(self, telegram_id, nickname, hobby, age, married, city, email_address, floor, photo):
        self.cursor.execute(
            sql_queries.INSERT_PROFILE_QUERY,
            (None, telegram_id, nickname, hobby, age, married, city, email_address, floor, photo)
        )
        self.connection.commit()

    def select_profiles(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'nickname': row[2],
            'hobby': row[3],
            'age': row[4],
            'married': row[5],
            'city': row[6],
            'email_address': row[7],
            'floor': row[8],
            'photo': row[9]
        }
        return self.cursor.execute(
            sql_queries.SELECT_LJ2_PROFILE_QUERY, (telegram_id, telegram_id, telegram_id)
        ).fetchall()

    def insert_like_profile(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY, (None, owner, liker,)
        )
        self.connection.commit()

    def insert_dislike_profile(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_DISLIKE_QUERY, (None, owner, liker,)
        )
        self.connection.commit()
