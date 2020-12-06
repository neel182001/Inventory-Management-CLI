# INVENTORY MANAGEMENT 

# ------------------------------- Importation --------------------------------

import os 
import mysql.connector 
import datetime 
now = datetime.datetime.now()


# -------------------------------- Functions ---------------------------------

def clrscr(): 
    print("\n"*5)


# --------------------------------- Classes ----------------------------------

class Management:
    
    def product_mgmt(n):
        while True:
            print("\t\t\t 1. Add New Product")    
            print("\t\t\t 2. List Product")             
            print("\t\t\t 3. Update Product")            
            print("\t\t\t 4. Delete Product")          
            print("\t\t\t 5. Back (Main Menu)")        
            p = int(input("\t\t Enter Your Choice :"))  
            if p == 1:                               
                prm.add_product()              
            if p == 2:                          
                prm.search_product()               
            if p == 3:                         
                prm.update_product()               
            if p == 4:                         
                prm.delete_product()                 
            if p == 5:                           
                break
            
    def purchase_mgmt(n):
        while True:
            print("\t\t\t 1. Add Order")      
            print("\t\t\t 2. List Order")                
            print("\t\t\t 3. Back (Main Menu)")        
            o = int(input("\t\t Enter Your Choice :"))       
            if o == 1:         
                pum.add_order()
            if o == 2:         
                pum.list_order()         
            if o == 3:                 
                break
            
    def sales_mgmt(n):
        while True:
            print("\t\t\t 1. Sale Items")
            print("\t\t\t 2. List Sales")
            print("\t\t\t 3. Back (Main Menu)")             
            s = int (input("\t\t Enter Your Choice :"))   
            if s == 1:
                sm.sale_product()
            if s == 2:
                sm.list_sale()
            if s == 3:
                break
            
    def user_mgmt(n):
        while True:
            print("\t\t\t 1. Add user")
            print("\t\t\t 2. List user")
            print("\t\t\t 3. Back (Main Menu)")
            u = int(input("\t\t Enter Your Choice :"))
            if u == 1:
                um.add_user()
            if u == 2:
                um.list_user()
            if u == 3:
                break
            
    def db_mgmt(n):
        while True:
            print("\t\t\t 1. Database creation")           
            print("\t\t\t 2. List Database")     
            print("\t\t\t 3. Back (Main Menu)")                   
            p = int(input("\t\t Enter Your Choice :"))           
            if p == 1:   
                d.create_database()             
            if p == 2:  
                d.list_database()         
            if p == 3: 
                break

class Database:
    
    def create_database():
        mydb = mysql.connector.connect(host='localhost',user='root',passwd='root')
        mycursor=mydb.cursor()
        print("Creating STOCK Database...")
        mycursor.execute("CREATE DATABASE if not exists Stock")
        print("STOCK Database Created\n")
        mydb = mysql.connector.connect(host='localhost',user='root',passwd='root',database='Stock')
        mycursor=mydb.cursor()
        print("Creating PRODUCT table...") 
        mycursor.execute("CREATE TABLE if not exists product (pcode int(4) PRIMARY KEY, pname char(30) NOT NULL,price float(8,2),pqty int(4),pcat char(30));")
        print("PRODUCT Table created\n")
        print("Creating ORDER table...")
        mycursor.execute("CREATE TABLE if not exists orders (orderid int(4)PRIMARY KEY, orderdate DATE,pcode char(30) NOT NULL ,pprice float(8,2),pqty int(4),supplier char(50),pcat char(30));")   
        print("ORDER table created\n")       
        print("Creating SALES table...")   
        mycursor.execute("CREATE TABLE if not exists sales (salesid int(4),salesdate DATE,pcode char(30) references product(pcode),pprice float(8,2),pqty int(4),Total double(8,2));")  
        print("SALES table created\n")
        print("Creating USER table...")    
        mycursor.execute("CREATE TABLE if not exists user (uid char(6) PRIMARY KEY,uname char(30) NOT NULL,upwd char(30));")           
        print("USER table created\n")
        
    def list_database():
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")     
        mycursor = mydb.cursor()    
        sql = "show tables;"         
        mycursor.execute(sql)   
        for i in mycursor:   
            print(i)   

class Product_Management:
    
    def add_product(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")       
        mycursor = mydb.cursor()  
        sql = "INSERT INTO product(pcode,pname,price,pqty,pcat) values(%s,%s,%s,%s,%s)"           
        code = int(input("\t\t Enter product code :"))
        search = "SELECT count(*) FROM product WHERE pcode=%s;"      
        val = (code,) 
        mycursor.execute(search,val)    
        for x in mycursor:             
            cnt = x[0]         
            if cnt == 0:     
                name = input("\t\t Enter product name :")       
                qty = int(input("\t\t Enter product quantity :"))      
                price = float(input("\t\t Enter product unit price :"))  
                cat = input("\t\t Enter Product category :")     
                val = (code,name,price,qty,cat)               
                mycursor.execute(sql,val)                   
                mydb.commit()    
            else:           
                print("\t\t Product already exist")
                
    def list_product(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")          
        mycursor = mydb.cursor()     
        sql = "SELECT * from product"         
        mycursor.execute(sql)   
        print("\t\t\t\t PRODUCT DETAILS")   
        print("\t\t", "-" * 55)   
        print("\t\t code    name     \tprice    quantity      category") 
        print("\t\t", "-" * 55)      
        for i in mycursor:      
            print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])         
            print("\t\t", "-" * 55)
            
    def update_product(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")
        mycursor = mydb.cursor()         
        code = int(input("Enter the product code :"))       
        qty = int(input("Enter the quantity :"))       
        sql = "UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
        val = (qty,code)      
        mycursor.execute(sql,val)       
        mydb.commit()          
        print("\t\t Product details updated")
        
    def delete_product(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")         
        mycursor=mydb.cursor()        
        code = int(input("Enter the product code :"))    
        sql = "DELETE FROM product WHERE pcode = %s;"    
        val = (code,)            
        mycursor.execute(sql, val)          
        mydb.commit()       
        print(mycursor.rowcount,"record(s) deleted")
        
    def search_product(n):
        while True:
            print("\t\t\t 1. List all product")          
            print("\t\t\t 2. List product code wise")                   
            print("\t\t\t 3. List product category wise")      
            print("\t\t\t 4. Back (Main Menu)")         
            s = int(input("\t\t Enter Your Choice :"))                    
            if s == 1:          
                prm.list_product()  
            if s == 2:      
                code=int(input(" Enter product code :"))    
                prm.list_prcode(code)   
            if s == 3:  
                cat=input("Enter category :")       
                prm.list_prcat(cat)   
            if s == 4:     
                break
            
    def list_prcode(code):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")
        mycursor = mydb.cursor()       
        sql = "SELECT * from product WHERE pcode=%s"            
        val = (code,)   
        mycursor.execute(sql, val)  
        print("\t\t\t\t PRODUCT DETAILS")  
        print("\t\t", "-" * 55)          
        print("\t\t code    name    price   quantity      category")    
        print("\t\t", "-" * 55)          
        for i in mycursor:       
            print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4]) 
            print("\t\t", "-" * 55)
            
    def list_prcat(cat):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")
        mycursor = mydb.cursor()
        print(cat)
        sql="SELECT * from product WHERE pcat =%s"
        val = (cat,)
        mycursor.execute(sql, val)
        clrscr()
        print("\t\t\t\t PRODUCT DETAILS")
        print("\t\t", "-" * 55)          
        print("\t\t code    name    price   quantity    category")      
        print("\t\t", "-" * 55)         
        for i in mycursor:    
            print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])  
            print("\t\t", "-" * 55)
    
class Purchase_Management:
    
    def add_order(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")
        mycursor = mydb.cursor()    
        now = datetime.datetime.now() 
        sql = "INSERT INTO orders (orderid, orderdate, pcode,pprice, pqty, supplier, pcat) values(%s,%s,%s,%s,%s,%s,%s)"
        code = int(input("Enter product code :"))  
        oid = now.year+now.month+now.day+now.hour+now.minute+now.second     
        qty = int(input("Enter product quantity : "))     
        price = float(input("Enter Product unit price: ")) 
        cat = input("Enter product category: ")
        supplier = input("Enter Supplier details: ")        
        val = (oid, now, code, price, qty, supplier, cat)    
        mycursor.execute(sql, val)    
        mydb.commit()
        
    def list_order(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")
        mycursor = mydb.cursor()        
        sql = "SELECT * from orders"   
        mycursor.execute(sql)       
        print("\t\t\t\t\t\t\t ORDER DETAILS")  
        print("-"*85)             
        print("orderid   |   date   |  product code  |  price  |  quantity  |   supplier   |  category  |")     
        print("-" * 85)       
        for i in mycursor:
            print(" ", i[0], "\t\t", i[1], " \t\t ", i[2], " \t ", i[3], " \t ", i[4], " \t ", i[5], " \t ", i[6])    
            print("-" * 85)

class Sales_Management:
    
    def sale_product(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")  
        mycursor = mydb.cursor()  
        pcode = int(input("Enter product code: "))  
        sql = "SELECT count(*) from product WHERE pcode=%s;"      
        val = (pcode,)    
        mycursor.execute(sql,val)   
        for x in mycursor:
            cnt = x[0] 
            if cnt != 0 :                     
                sql = "SELECT * from product WHERE pcode=%s;"             
                val = (pcode,)       
                mycursor.execute(sql, val)          
                for x in mycursor:                   
                    print(x)             
                    price = int(x[2])    
                    pqty = int(x[3])                              
                    qty = int(input("Enter no of quantity :"))   
                    if qty <= pqty:      
                        total = qty * price 
                        print("Collect Rs. ", total)
                        sql = "INSERT into sales values(%s,%s,%s,%s,%s,%s)"  
                        val = (int(cnt)+1,datetime.datetime.now(),pcode,price,qty,total)                   
                        mycursor.execute(sql,val)
                        sql = "UPDATE product SET pqty=pqty-%s WHERE pcode=%s"   
                        val = (qty, pcode)         
                        mycursor.execute(sql, val)    
                        mydb.commit()            
                    else:     
                        print("Quantity not available") 
            else:
                print("Product is not available")
                
    def list_sale(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")   
        mycursor = mydb.cursor()    
        sql = "SELECT * FROM sales"    
        mycursor.execute(sql)   
        print("\t\t\t\t SALES DETAILS")          
        print("-" * 80)          
        print("Sales ID    Date    Product Code    Price        Quantity        Total")           
        print("-" * 80)          
        for x in mycursor:                   
            print(x[0], "\t", x[1], "\t", x[2], "\t", x[3], "\t\t", x[4], "\t\t", x[5])
            print("-" * 80)

class User_Management:
    
    def add_user(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")          
        mycursor = mydb.cursor()          
        uid = input("Enter emaid id :")  
        name = input("Enter Name :")   
        password = input("Enter Password :") 
        sql = "INSERT INTO user values (%s,%s,%s);"    
        val = (uid, name, password)       
        mycursor.execute(sql, val)        
        mydb.commit()             
        print(mycursor.rowcount, "user created")
        
    def list_user(n):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="stock")        
        mycursor = mydb.cursor()      
        sql = "SELECT uid, uname from user"   
        mycursor.execute(sql)           
        clrscr()         
        print("\t\t\t\t USER DETAILS")     
        print("\t\t", "-" * 2)
        print("\t\t UID        name    ")    
        for i in mycursor:
            print("\t\t", i[0], "\t", i[1])
            print("\t\t", "-" * 27)

m = Management()
d = Database()
prm = Product_Management()
pum = Purchase_Management()
sm = Sales_Management()
um = User_Management() 


# -------------------------------- __Main__ ----------------------------------

while True:        
     clrscr()      
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
         m.product_mgmt()      
     if n == 2:          
         os.system('cls')
         m.purchase_mgmt() 
     if n == 3:
         m.sales_mgmt()
     if n == 4:
         m.user_mgmt()
     if n == 5:
         m.db_mgmt()
     if n == 6:
         break
         
