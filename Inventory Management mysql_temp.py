# INVENTORY MANAGEMENT 

# ------------------------------- Importation --------------------------------

from management import Management
import os


# -------------------------------- Inventory Management ---------------------------------

class InventoryManagement(Management):

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.clrscr()
            print("STOCK MANAGEMENT")
            print("****************\n")
            print("1. PRODUCT MANAGEMENT")
            print("2. PURCHASE MANAGEMENT")
            print("3. SALES MANAGEMENT")
            print("4. USER MANAGEMENT")
            print("5. DATABASE SETUP")
            print("6. EXIT\n")
            n = int(input("Enter your choice :"))
            if n == 1:
                self.product_mgmt()
            if n == 2:
                os.system('cls')
                self.purchase_mgmt()
            if n == 3:
                self.sales_mgmt()
            if n == 4:
                self.user_mgmt()
            if n == 5:
                self.db_mgmt()
            if n == 6:
                break


if __name__ == "__main__":
    inMgmt = InventoryManagement()
    inMgmt.run()
