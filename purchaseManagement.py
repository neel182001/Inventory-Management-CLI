# ------------------ Importations -------------------
import os, platform, datetime
from database import Database
from prettytable import PrettyTable


# ----------------Purchase Management ---------------------
class PurchaseManagement(Database):

    def __init__(self):
        super().__init__()
        self.now = datetime.datetime.now()

    def clrscr(self):
        if platform.system() == "Windows":
            os.system("cls")

    def add_order(self):
        sql = """INSERT INTO orders (orderid, orderdate, pcode, pprice, pqty, supplier, pcat) 
                 values(?, ?, ?, ?, ?, ?, ?)"""
        code = int(input("Enter product code :"))
        oid = self.now.year + self.now.month + self.now.day + self.now.hour + self.now.minute + self.now.second
        qty = int(input("Enter product quantity : "))
        price = float(input("Enter Product unit price: "))
        cat = input("Enter product category: ")
        supplier = input("Enter Supplier details: ")
        val = (oid, self.now, code, price, qty, supplier, cat)
        self.dbCursor.execute(sql, val)
        self.con.commit()

    def list_order(self):
        sql = "SELECT * from orders"
        self.dbCursor.execute(sql)
        data = self.dbCursor.fetchall()
        table = PrettyTable(['Order Id', 'Date', 'Product Code', 'Price', 'Quantity', 'Supplier', 'Category'])
        for rec in data:
            table.add_row(rec)
        print("\t\t\t\t\t\t\t ORDER DETAILS")
        print(table)
