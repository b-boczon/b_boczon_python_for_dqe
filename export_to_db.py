import pyodbc

# path to db
db_path = "./newsfeed_db.db"

class ToDB:

    def __init__(self, db_path):
        # Establish a connection to the database using the SQLite3 ODBC Driver
        with pyodbc.connect(f'DRIVER={{SQLite3 ODBC Driver}};DATABASE={db_path};') as self.connection: 
            self.cursor = self.connection.cursor()

    # Method to create tables in the database if they do not already exist with autoincrementing primary key id
    def create_tables(self):
        self.cursor.execute("""create table if not exists news (
                            news_id integer primary key autoincrement,
                            content text,
                            city text,
                            publish_datetime datetime)""")

        self.cursor.execute("""create table if not exists private_ad (
                            ad_id integer primary key autoincrement,
                            content text,
                            actual_until date,
                            days_left integer)""")

        self.cursor.execute("""create table if not exists score (
                            match_id integer primary key autoincrement,
                            team1 text,
                            score text,
                            team2 text)""")
        
        # Commit the changes to the database 
        self.connection.commit()

    # Method to insert a record into news table in the database without duplicates using where not exists
    def insert_news(self, text, city, date):
        self.cursor.execute(""" insert into news (content, city, publish_datetime) 
                                select ?, ?, ?
                                where not exists (  select 1
                                                    from news
                                                    where content = ?
                                                    and city = ?
                                                    and publish_datetime = ?
                                                )""",
                            (text, city, date, text, city, date))
        # commit after entry
        self.connection.commit()

    # Method to insert a record into private_ad table in the database without duplicates using where not exists
    def insert_private_ad(self, text, exp_date, days_left):
        self.cursor.execute(""" insert into private_ad (content, actual_until, days_left) 
                                select ?, ?, ?
                                where not exists (  select 1
                                                    from private_ad
                                                    where content = ?
                                                    and actual_until = ?
                                                    and days_left = ?
                                                )""",
                            (text, exp_date, days_left, text, exp_date, days_left))
        # commit after entry
        self.connection.commit()

    # Method to insert a record into score table in the database without duplicates using where not exists
    def insert_score(self, team1, score, team2):
        self.cursor.execute(""" insert into score (team1, score, team2)
                                select ?, ?, ?
                                where not exists (  select 1
                                                    from score
                                                    where team1 = ?
                                                    and score = ?
                                                    and team2 = ?
                                                )""",
                            (team1, score, team2, team1, score, team2))
        # commit after entry
        self.connection.commit()
