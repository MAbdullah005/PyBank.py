class Customer:
    def __init__(self):
        self.name=""
        self.last_name=""
        self.brith_date=datetime.date
        self.cnic=int
        self.adress=""
        self.city=""
        self.country=""
        self.age=int

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
          while self.check_cnic_duplication(int(self.cnic)):
              print("\nEnter a correct cnic or -1 ")
              self.cnic=int(input("Enter a Cnic "))  
              if self.cnic==-1:
                  exit()
        except ValueError as e:
           print("Expection occure cnic is int type")
        self.adress=input("Enter a adress ")
        self.city=input("Enter a city ")
        self.country=input("Enter a country name ")
        self.age=int(abs((datetime.date.today()-self.brith_date).days/365))
        print("person age is ",self.age)

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

