
class Account:
    
    def __init__(self,cnic) -> None:

        self.name=""
        self.email=""
        self.last_name=""
        self.account_number=""
        self.created_date=""
        self.expire_date=""
        self.password=""
        self.cnic=cnic 
        self.balance=0
        

        # Create account
        def Create_account(self):
    name=input("Enter a First name ")
    last_name=input("Enter a last name ")
    self.created_date=datetime.date.today()
    self.expire_date=datetime.date(2035,9,10)
    print("Created date ",self.created_date)
    print("Expire date ",self.expire_date)
    #---
    mail=input("Enter a Email ")
    mail1=input("comfrim the email ")
    while mail!=mail1 or self.check_email_duplication(mail):
        print("\nEnter a correct email please or esc ")
        mail=input("Enter a Email ")
        mail1=input("comfrim the email ")

     # generate code for user email varification
  
    code1=self.generate_code()

     # Send Email to login user

    self.send_Email(code1,mail)

    # Conformation code for user login

    self.Conformation_code(code1,mail)

    # Password managere for security check password is in correct format

    self.Password_manage()

    # get account number after you sucessfuly login to email

    self.get_account_number()
    # assinging the attributes
    self.name,self.last_name,self.email,=name,last_name,mail

    # Update the data base for new user that newly ogin
    
    try:
      data=[self.name,self.last_name,str(self.cnic),self.created_date.isoformat(),self.expire_date.isoformat(),self.email,self.password,self.account_number]
      with sqlite3 .connect("data.db") as conn:
       command = '''INSERT INTO DATA ("Name", "Last Name", "Cnic", "Created Date", "Expire Date", "Email", "Passwrd", "Account Number") VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
       conn.execute(command,data)
       conn.commit()
    
    except TypeError as e:
        print("Type error expection occure ")
    finally:
        if 'conn' in locals():
          conn.close()  # Ensure connection is closed
          print("Database operation complete.")

   #---

    # Done status to Ture which represent that account is succfuly login
   
    self.status=True
    print("Here are your account number ",self.account_number)
    print("Your account status is active",self.status)

    # Function to check if the duplicated email is in the 
     # databse if the email is exist user enter to email 
     # again until enter a correct email 
    def check_email_duplication(self,mail)->bool:
      with sqlite3.connect("data.db") as conn:
         command="SELECT Email FROM Data"
         cursor=conn.execute(command)
         for row in cursor:
            if row[0]==mail:
                self.blink_message("This email is already registered")
                return True
      return False


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


 def get_account_number(self):
     account=["1","2","3","4"]
     account_num=""
     for a in range(1):
        account_num+=random.choice(account)
        print("a",a," ..",account_num)

     while self.Check_account_num(account_num):
          account_num=""
          for a in range(1):
           account_num+=random.choice(account)
     self.account_number=account_num

 def Password_manage(self):

     pas=input("Enter a password ")
     self.password=input("Enter a password for conformation ")
     if pas!=self.password:
         while True:
              self.blink_message("             Please enter a corect Password")
              pas=input("\nEnter a password ")
              self.password=input("Enter a password for conformation ")
              if pas==self.password:
                break
