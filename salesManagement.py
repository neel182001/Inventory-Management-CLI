import sqlite3
import datetime
from prettytable import PrettyTable


class SalesManagement:

    def __init__(self):
        self.con = sqlite3.connect("Data/stock.db")
        self.dbCursor = self.con.cursor()

    def sale_product(self):
        pcode = int(input("Enter product code: "))
        sql = "SELECT count(*) from product WHERE pcode = ?;"
        val = (pcode,)
        self.dbCursor.execute(sql, val)
        for x in self.dbCursor:
            cnt = x[0]
            if cnt != 0:
                sql = "SELECT * from product WHERE pcode = ?;"
                val = (pcode,)
                self.dbCursor.execute(sql, val)
                for product in self.dbCursor:
                    print(product)
                    price = int(product[2])
                    pqty = int(product[3])
                    qty = int(input("Enter no of quantity :"))
                    if qty <= pqty:
                        total = qty * price
                        print("Collect Rs. ", total)
                        sql = "INSERT into sales values(?, ?, ?, ?, ?, ?)"
                        val = (int(cnt) + 1, datetime.datetime.now(), pcode, price, qty, total)
                        self.dbCursor.execute(sql, val)
                        sql = "UPDATE product SET pqty= pqty - ? WHERE pcode = ?"
                        val = (qty, pcode)
                        self.dbCursor.execute(sql, val)
                        self.con.commit()
                    else:
                        print("Quantity not available")
            else:
                print("Product is not available")

    def list_sale(self):
        sql = "SELECT * FROM sales"
        self.dbCursor.execute(sql)
        data = self.dbCursor.fetchall()
        table = PrettyTable(['Sales Id', 'Date', 'Product Code', 'Price', 'Quantity', 'Total'])
        for rec in data:
            table.add_row(rec)
        print("\t\t\t\t SALES DETAILS")
        print(table)
