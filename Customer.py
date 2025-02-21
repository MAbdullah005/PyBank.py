
class Customer:
    def __init__(self):
        self.name=string
        self.last_name=string
        self.brith_date=datetime.date
        self.cnic=int
        self.adress=string
        self.city=string
        self.country=string
        self.age=string

        # Enter a information abouth a preson
        # that gone be a user for bank and 
        # bank account or both

    def enter_info(self):
        print("\n")
        self.name=(input("Enter a your name "))
        self.last_name=input("Enter a last name ")
        try:
          year=int(input("entre a yaer "))
          month=int(input("Enter a month "))
          day=int(input("Enter a day "))
          self.brith_date=datetime.date(year,month,day)
          print(self.brith_date)
        except ValueError as e:
          print("Expection occure")  
          exit()
        try:
          self.cnic=int(input("Enter a cnic "))
          #while self.check_cnic_duplication(int(self.cnic)):
           #   print("\nEnter a correct cnic or -1 ")
            #  self.cnic=int(input("Enter a Cnic "))  
             # if self.cnic==-1:
              #    exit()
        except ValueError as e:
           print("Expection occure cnic is int type")
        self.adress=input("Enter a adress ")
        self.city=input("Enter a city ")
        self.country=input("Enter a country name ")
        self.age=int(abs((datetime.date.today()-self.brith_date).days/365))
        print("person age is ",self.age)

        try:
          data=[str(self.cnic),self.name,self.last_name,self.brith_date.isoformat(),self.adress,self.city,self.country,self.age]
          with sqlite3.connect("DataBase.db") as conn:
  
              command='''INSERT INTO CUSTOMER ("Cnic", "Name", "Last Name", "Age", "Brith Date", "Address", "City", "Country") VALUES (?,?,?,?,?,?,?,?)'''
              conn.execute(command,data)
              conn.commit()     
        
        except TypeError as e:
            print("Type error expection occure ")
        finally:
            if 'conn' in locals():
              conn.close()  # Ensure connection is closed
              print("Database operation complete.")

        # update any attribute of he person class 
        # Depedent on a choice 

    def Update_info(self):
        print("\n")
        choice=input("What you want to update ")
        if choice == "Name":
           self.name=(input("Enter a your name "))
           self.last_name=input("Enter a last name ")
        elif choice=="adress":
             self.adress=input("Enter a adress ")
             self.city=input("Enter a city ")
             self.country=input("Enter a country name ")
        elif choice=="cnic":
            self.cnic=input("enter a cnic ")
        elif choice=="brith date":
            try:
                year=int(input("entre a yaer "))
                month=int(input("Enter a month "))
                day=int(input("Enter a day "))
                self.brith_date=datetime.date(year,month,day)
                print(self.brith_date)
            except ValueError as e:
               print("Expection occure")  
               exit()
        elif choice=="exit" or choice=="esc" or choice=="0":
            print("esc the function sucessfully \n")


    def check_cnic_duplication(self,cnic)->bool:
         
         with sqlite3.connect("data.db") as conn:
       
            command="SELECT Cnic FROM Data"
            cursor=conn.execute(command)
            for row in cursor:
               if row[0]==(cnic):
                   print(row[0],"Why")
                   self.blink_message("This Cnic is already registered")
                   return True
            return False

    def blink_message(self, message):
        for _ in range(2): 
            sys.stdout.write("\r" + message)  
            sys.stdout.flush()  
            time.sleep(0.5)  
            sys.stdout.write("\r" + " " * len(message)) 
            sys.stdout.flush() 
            time.sleep(0.5)  


    def show_info(self):
        print("\n")
        print("To show any person or usre information \n please enter a required field ")
        cnic=input("Enter a your cnic ")
        if self.cnic==cnic:
            print("Here is the person information \n based on thier cnic ")
            print("Person Nmae ",self.name)
            print("Person last Name ",self.last_name)
            print("Person cnic ",self.cnic)
            print("Person city ",self.city)
            print("Person country ",self.country)
            print("Person Address ",self.adress)
            print("Person Brith date ",self.brith_date)
            print("Person age ",self.age)
