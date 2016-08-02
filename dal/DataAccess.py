import settings
import psycopg2

class DataAccessor():
    conn = None
    cur = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database=settings.DATABASES['postgreSQL']['name'],
                user=settings.DATABASES['postgreSQL']['user'],
                password=settings.DATABASES['postgreSQL']['password'],
                host=settings.DATABASES['postgreSQL']['host']
            )
            self.cur = self.conn.cursor()
        except:
            print('unable to connect DB')





















    #*************************************
    def creteable(self):
        cur = self.conn.cursor()
        cur.execute(self.initialquery)
        self.conn.commit()
    def select(self):

        self.cur.execute("""INSERT INTO users (Name, lname,username,password,active) VALUES('ROma','Alimovv', 'alimov@tillo', 'kymbatIsMyLove', True);""")
        self.conn.commit()
        self.cur.execute("""select * FROM users;""")
        rows = self.cur.fetchall()
        print('SELECT * ')
        for row in rows:
            print ( "id = ", row[0])
            print ( "name = ", row[1])
            print ( "lname = ", row[2])
            print ( "username = ", row[3])
            print ( "password = ", row[4])
            print ( "active = ", row[5],"\n")
        self.conn.close()


    def insert(self):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Cars2 (Name, Price) VALUES('Audi',52642)")
        cur.execute("INSERT INTO Cars2 (Name, Price) VALUES('Mercedes',57127)")
        self.conn.commit()
        print('insert into ')



    initialquery = """CREATE TABLE users(
id SERIAL PRIMARY KEY,
name VARCHAR(50),
lname VARCHAR(50),
username VARCHAR(50),
password VARCHAR(50),
active BOOLEAN
);

CREATE TABLE posts(
id SERIAL PRIMARY KEY,
title VARCHAR(200),
post TEXT
);


CREATE TABLE likes(
id SERIAL PRIMARY KEY,
user_id integer REFERENCES users (id),
post_id integer REFERENCES posts (id)
);



    """












