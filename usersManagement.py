import sqlite3
import os, platform
from prettytable import PrettyTable


def clrscr():
    if platform.system() == "Windows":
        os.system("cls")


class UsersManagement:

    def __init__(self):
        self.con = sqlite3.connect("Data/stock.db")
        self.dbCursor = self.con.cursor()

    def add_user(self):
        uid = str(input("Enter emaid id :"))
        name = str(input("Enter Name :"))
        password = str(input("Enter Password :"))
        sql = "INSERT INTO user values (?, ?, ?);"
        val = (uid, name, password)
        self.dbCursor.execute(sql, val)
        self.con.commit()
        print(self.dbCursor.rowcount, "user created")

    def list_user(self):
        sql = "SELECT uid, uname from user"
        self.dbCursor.execute(sql)
        clrscr()
        data = self.dbCursor.fetchall()
        table = PrettyTable(['UID', 'Name'])
        for rec in data:
            table.add_row(rec)
        print("\t\t\t\t USER DETAILS")
        print(table)
