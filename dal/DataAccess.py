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
        self.cur.execute(self.initialquery)
        self.conn.commit()
    def selectExample(self):
        self.cur.execute("""select * FROM users;""")
        rows = self.cur.fetchall()
        print('SELECT * ', len(rows))
        for row in rows:
            print ( "id = ", row[0])
            print ( "name = ", row[1])
            print ( "lname = ", row[2])
            print ( "username = ", row[3])
            print ( "password = ", row[4])
            print ( "active = ", row[5])
            self.cur.execute("select session FROM sessions where id_user = '%s';" % row[0])
            ro = self.cur.fetchall()
            for j in ro:
                print("    cookie =",j[0])
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")



    def select(self,query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def update(self,query):
        self.cur.execute(query)
        self.conn.commit()


    def insert(self,table,**kwargs):
        query = "INSERT INTO %s" % table
        variable = ""
        values = ""
        for i in kwargs:
            variable+=(" " + str(i) + " , ")
            values+=("'" +str( kwargs[i]) + "', ")
        query = ("%s (%s) values (%s)" % (query, variable[:-2], values[:-2]))
        self.cur.execute(query)
        self.conn.commit()


    def is_exist_user(self,username):
        self.cur.execute("select * FROM users where username = '%s';" % username.lower())
        rows = self.cur.fetchall()
        if len(rows)>0:
            return True
        else:
            return False

    def delete(self,table, **kwargs):
        query = "DELETE FROM %s " % table
        variable = ""
        for i in kwargs:
            variable += (" " + str(i) + " = '" + str(kwargs[i]+"', " ))
        query = ("%s where %s;" % (query, variable[:-2]))
        self.cur.execute(query)
        self.conn.commit()


    initialquery = """DROP TABLE sessions, users, posts, likes;
CREATE TABLE users(
id SERIAL PRIMARY KEY,
name VARCHAR(50),
lname VARCHAR(50),
username VARCHAR(50),
password VARCHAR(50),
active BOOLEAN
);

CREATE TABLE sessions(
id SERIAL PRIMARY KEY,
id_user integer REFERENCES users (id),
session VARCHAR(200)
);

CREATE TABLE posts(
id SERIAL PRIMARY KEY,
user_id integer REFERENCES users (id),
title VARCHAR(200),
post TEXT
);


CREATE TABLE likes(
id SERIAL PRIMARY KEY,
user_id integer REFERENCES users (id),
post_id integer REFERENCES posts (id)
);



    """












