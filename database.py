import sqlite3
import random

class Database:

    DB_NAME = "facts.db"

    def __init__(self):
        """ Connects to database. Creates the database if it doesn't already exist. Creates a facts table if it doesn't already exist. """
        self.conn = sqlite3.connect(Database.DB_NAME)
        self.make_table()

    def make_table(self):
        """ Creates the facts table if it doesn't already exist. Table consists only of a primary key and short string. """
        curs = self.conn.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS facts(id INTEGER PRIMARY KEY AUTOINCREMENT, txt VARCHAR(255) NOT NULL)")
        curs.close()
        self.conn.commit()

    def insert(self,text:str):
        """ Inserts a fact into the database """
        #TODO Sanitize input

        if "'" in text:
            text = text.replace("'",'"')

        cmd = "INSERT INTO facts(txt) VALUES ('{}');".format(text)
        print(cmd)
        curs = self.conn.cursor()
        curs.execute(cmd)
        curs.close()
        self.conn.commit()

    def get_fact(self,key:int) -> str:
        """ Gets a fact from the database using it's primary key """
        cmd = "SELECT txt FROM facts WHERE id='{}';".format(key)
        curs = self.conn.cursor()
        curs.execute(cmd)
        res = curs.fetchone()[0]

        assert type(res) == str, "Result from database must be a string, had type: {}".format(type(res))

        return res

    def get_num_rows(self,) -> int:
        """ Returns the number of rows in the only table we care about """
        curs = self.conn.cursor()
        curs.execute("SELECT COUNT(*) FROM facts;")
        res = int(curs.fetchone()[0])
        return res

    def get_random_fact(self) -> str:
        """ Gets a random fact from the database. This implements the purpose of this project. """
        num_rows = self.get_num_rows()
        index = random.randint(1,num_rows)
        return self.get_fact(index)

    def close(self):
        self.conn.close()

def get_random_fact():
    """ Wrapper for making a database connection object and getting an object """
    db = Database()
    res = db.get_random_fact()
    db.close()
    return res

