from purchaseManagement import PurchaseManagement
from prettytable import PrettyTable


class ProductManagement(PurchaseManagement):

    def __init__(self):
        super().__init__()

    def add_product(self):
        code = int(input("\t\t Enter product code :"))
        search = f"""SELECT count(*) FROM product WHERE pcode = "{code}";"""
        self.dbCursor.execute(search)
        sql = "INSERT INTO product(pcode, pname, price, pqty, pcat) values(?, ?, ?, ?, ?)"
        for x in self.dbCursor:
            cnt = x[0]
            if cnt == 0:
                name = input("\t\t Enter product name :")
                qty = int(input("\t\t Enter product quantity :"))
                price = float(input("\t\t Enter product unit price :"))
                cat = input("\t\t Enter Product category :")
                val = (code, name, price, qty, cat)
                self.dbCursor.execute(sql, val)
                self.con.commit()
            else:
                print("\t\t Product already exist")

    def list_product(self):
        sql = "SELECT * from product"
        self.dbCursor.execute(sql)
        data = self.dbCursor.fetchall()
        table = PrettyTable(['Code', 'Name', 'Price', 'Quantity', 'Category'])
        for rec in data:
            table.add_row(rec)
        print("\t\t\t\t PRODUCT DETAILS")
        print(table)

    def update_product(self):
        code = int(input("Enter the product code :"))
        qty = int(input("Enter the quantity :"))
        sql = "UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
        val = (qty, code)
        self.dbCursor.execute(sql, val)
        self.con.commit()
        print("\t\t Product details updated")

    def delete_product(self):
        code = int(input("Enter the product code :"))
        sql = "DELETE FROM product WHERE pcode = ?;"
        val = (code,)
        self.dbCursor.execute(sql, val)
        self.con.commit()
        print(self.dbCursor.rowcount, "record(s) deleted")

    def search_product(self):
        while True:
            print("\t\t\t 1. List all product")
            print("\t\t\t 2. List product code wise")
            print("\t\t\t 3. List product category wise")
            print("\t\t\t 4. Back (Main Menu)")
            s = int(input("\t\t Enter Your Choice :"))
            if s == 1:
                self.list_product()
            if s == 2:
                code = int(input(" Enter product code :"))
                self.list_prcode(code)
            if s == 3:
                cat = input("Enter category :")
                self.list_prcat(cat)
            if s == 4:
                break

    def list_prcode(self, code):
        sql = "SELECT * from product WHERE pcode = ?"
        val = (code,)
        self.dbCursor.execute(sql, val)
        data = self.dbCursor.fetchall()
        table = PrettyTable(['Code', 'Name', 'Price', 'Quantity', 'Category'])
        for rec in data:
            table.add_row(rec)
        print("\t\t\t\t PRODUCT DETAILS")
        print(table)

    def list_prcat(self, cat):
        print(cat)
        sql = "SELECT * from product WHERE pcat = ?"
        val = (cat,)
        self.dbCursor.execute(sql, val)
        self.clrscr()
        data = self.dbCursor.fetchall()
        table = PrettyTable(['Code', 'Name', 'Price', 'Quantity', 'Category'])
        for rec in data:
            table.add_row(rec)
        print("\t\t\t\t PRODUCT DETAILS")
        print(table)
