from productManagement import ProductManagement
from salesManagement import SalesManagement
from usersManagement import UsersManagement


class Management(ProductManagement):

    def __init__(self):
        super().__init__()
        self.salesMgmt = SalesManagement()
        self.userMgmt = UsersManagement()

    def product_mgmt(self):
        while True:
            print("\t\t\t 1. Add New Product")
            print("\t\t\t 2. List Product")
            print("\t\t\t 3. Update Product")
            print("\t\t\t 4. Delete Product")
            print("\t\t\t 5. Back (Main Menu)")
            p = int(input("\t\t Enter Your Choice :"))
            if p == 1:
                self.add_product()
            if p == 2:
                self.search_product()
            if p == 3:
                self.update_product()
            if p == 4:
                self.delete_product()
            if p == 5:
                break

    def purchase_mgmt(self):
        while True:
            print("\t\t\t 1. Add Order")
            print("\t\t\t 2. List Order")
            print("\t\t\t 3. Back (Main Menu)")
            o = int(input("\t\t Enter Your Choice :"))
            if o == 1:
                self.add_order()
            if o == 2:
                self.list_order()
            if o == 3:
                break

    def sales_mgmt(self):
        while True:
            print("\t\t\t 1. Sale Items")
            print("\t\t\t 2. List Sales")
            print("\t\t\t 3. Back (Main Menu)")
            s = int(input("\t\t Enter Your Choice :"))
            if s == 1:
                self.salesMgmt.sale_product()
            if s == 2:
                self.salesMgmt.list_sale()
            if s == 3:
                break

    def user_mgmt(self):
        while True:
            print("\t\t\t 1. Add user")
            print("\t\t\t 2. List user")
            print("\t\t\t 3. Back (Main Menu)")
            u = int(input("\t\t Enter Your Choice :"))
            if u == 1:
                self.userMgmt.add_user()
            if u == 2:
                self.userMgmt.list_user()
            if u == 3:
                break

    def db_mgmt(self):
        while True:
            print("\t\t\t 1. Database creation")
            print("\t\t\t 2. List Database")
            print("\t\t\t 3. Back (Main Menu)")
            p = int(input("\t\t Enter Your Choice :"))
            if p == 1:
                self.create_database()
            if p == 2:
                self.list_database()
            if p == 3:
                break
