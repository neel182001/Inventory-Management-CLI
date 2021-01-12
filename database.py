import sqlite3
import os


class Database:

    def __init__(self):
        self.existence = os.path.exists("Data")
        if not self.existence:
            os.mkdir("Data")
            self.con = sqlite3.connect("Data/stock.db")
            self.dbCursor = self.con.cursor()
            self.create_database()
        else:
            self.con = sqlite3.connect("Data/stock.db")
            self.dbCursor = self.con.cursor()

    def create_database(self):
        print("Creating PRODUCT table...")
        self.dbCursor.execute("""CREATE TABLE if not exists product 
                                (pcode int(4) PRIMARY KEY, 
                                pname char(30) NOT NULL,
                                price float(8,2),
                                pqty int(4),
                                pcat char(30));""")
        self.con.commit()
        print("PRODUCT Table created\n")
        print("Creating ORDER table...")
        self.dbCursor.execute("""CREATE TABLE if not exists orders 
                                (orderid int(4)PRIMARY KEY, 
                                orderdate DATE,
                                pcode char(30) NOT NULL ,
                                pprice float(8,2),
                                pqty int(4),
                                supplier char(50),
                                pcat char(30));""")
        self.con.commit()
        print("ORDER table created\n")
        print("Creating SALES table...")
        self.dbCursor.execute("""CREATE TABLE if not exists sales 
                                (salesid int(4),
                                salesdate DATE,
                                pcode char(30) references product(pcode),
                                pprice float(8,2),
                                pqty int(4),
                                Total double(8,2));""")
        self.con.commit()
        print("SALES table created\n")
        print("Creating USER table...")
        self.dbCursor.execute("""CREATE TABLE if not exists user 
                                (uid char(6) PRIMARY KEY,
                                uname char(30) NOT NULL,
                                upwd char(30));""")
        self.con.commit()
        print("USER table created\n")

    def list_database(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        self.dbCursor.execute(sql)
        for table in (self.dbCursor.fetchall()):
            print(table)
