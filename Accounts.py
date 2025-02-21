
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

     def Conformation_code(self,code1,reciver):

        confrim_code="G-"
        confrim_code+=input("Enter a conformation code ")
        while confrim_code!=code1:
            print("wrong code enter again \n resend code enter resend \n  Esc for quit")
            confrim_code=input()
            if confrim_code.lower()=="resend":
                self.send_Email(code1,reciver)
            elif confrim_code.lower()=="esc":
                exit()

        print("You are sucessfully sign on applicaion ")

    def generate_code(self):

        code=["1","2","3","4","5","6","7","8","9","0"]
        code1="G-"
        for a in range(5):
           code1+=random.choice(code)

        return code1

    # Senf email to 

    def send_Email(self,code1,receiver_email):

        sender_email = "abdullahaliofc@gmail.com"
        password = "vkoaeswdmspdjkau"

# Set up the message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Test Email from Python"

# Email body (can be plain text or HTML)
        body = "This is a test email sent from Python! \n your code for conformation is "+code1
        msg.attach(MIMEText(body, 'plain'))

# Connect to Gmail's SMTP server
        try:
               with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.starttls()  # Encrypt the connection
                smtp.login(sender_email, password)  # Log in to the SMTP server
                smtp.sendmail(sender_email, receiver_email, msg.as_string())  # Send email
                print("Email sent successfully!")
        except Exception as e:
               print(f"An error occurred: {e}")

             # Check account Function

    def Check_account_num(self,account_num)->bool:
         with Path("D:\\python.pyt\\PythonApplication1\\file.text") as path:
          for a in path.read_text():
            if a==account_num:
                self.blink_message("This account number alredy register get another one")
                return True
         path.write_text(account_num)
         return False
        

    def Show_info(self):
        mail=input("Enter your email ")
        pas=input("Enter a Password ")
        if mail==self.email:
            if pas==self.password:

              print("Here are your Account Information ")
              print("Account number ",self.account_number)
              print("Account Name ",self.name)
              print("Last name ",self.last_name)
              print("Created date ",self.created_date)
              print("Expire Date ",self.expire_date)
              print("Current Status ",self.status)
              print("Email ",self.email)
              print("Password ",self.email)
              print("Status type ",self.status)
            else:
                self.blink_message("Enter a correct password ")
        else:
            self.blink_message("Please enter a correct email ")

    def de_active_account(self):
        if self.status==True:

          mail=input("Enter your email ")
          pas=input("Enter a your password ")
          if mail==self.email:
             if pas==self.password:

              print("Here are your Account Information ")
              print("Account number ",self.account_number)
              print("Account Name ",self.name)
              print("Last name ",self.last_name)
              print("Created date ",self.created_date)
              print("Expire Date ",self.expire_date)
              print("Current Status ",self.status)
              print("Email ",self.email)
              print("Password ",self.email)
              print("Status type ",self.status)
              y=input("Press y to deactive your account ")
              if y.lower()=="yes":
                  self.status=False
                  print("Your account sucessufy deactivate ")
                  print("Now you are not allowed to do any transaction ")
                  print("for transaction you need to active your account")
             else:
                self.blink_message("Enter a correct password ")
          else:
            self.blink_message("Please enter a correct email ")
        else:
            print("Your account alredy deactive ")
    # Active account Function

    def active_account(self):
        if self.status==True:

          mail=input("Enter your email ")
          pas=input("Enter a your password ")
          if mail==self.email:
             if pas==self.password:

              print("Here are your Account Information ")
              print("Account number ",self.account_number)
              print("Account Name ",self.name)
              print("Last name ",self.last_name)
              print("Created date ",self.created_date)
              print("Expire Date ",self.expire_date)
              print("Current Status ",self.status)
              print("Email ",self.email)
              print("Password ",self.email)
              print("Status type ",self.status)
              y=input("Press y to Active your account ")
              if y.lower()=="yes":
                  self.status=False
                  print("Your account sucessufy Activated ")
                  print("Now you are allowed to do any transaction ")
                  print("For stop transaction you need to Deactive your account")
             else:
                self.blink_message("Enter a correct password ")
          else:
            self.blink_message("Please enter a correct email ")
        else:
            print("Your account alredy Active ")
    # Deposit  amouth

    def deposit(self):
       if self.status==True:
        try:

            cnic=int(input("Enter a cnic "))
            if self.cnic==cnic:
              print("Name ",self.name," ",self.last_name)
              while True:
                try:
                 balanc= int(input("Enter a amouth to Deposit "))
                 if balanc <0:
                     print("No Amouth accpted less than zero (0)")
                 else:
                   self.balance=self.balance+balanc  
                   print("Deposit  transaction done")
                   break
                except ValueError  as e:
                 print("Expection occure")
            else:
                print("No bank account found ")
        except ValueError as e:
             print("Expection occure")
       else:
           print("Your account is Deactive \n No action will be done until \n You inactve the account")

     # With draw amouth
    def withdraw(self):
      if self.status==True:
        print("Enter a cnic ")
        try:
            cnic=int(input())
            pas=input("Enter a Password ")
            if cnic==self.cnic and pas==self.password:
                 try:
                   balance = int(input("Enter a number "))
                   if balance<0:
                       print("No with drawn accpted ")
                   elif balance>self.balance:
                       print("Not balance insufficant")
                   elif balance>50000:
                       print("much $ than limit withdraw Fail")
                   else:
                       self.balance-=balance
                       print("Withdraw money done ")
                 except ValueError  as e:
                   print("Expection occure")
            else:
                print("No account found or incorrect cnic ")
        except ValueError as e:
            print("Expection occure")
      else:
          print("Your account is Deactive \n No action will be done until \n You inactve the account")
          
    # Check balance
    def Check_balance(self):
      if self.status==True:
        print("Enter a Cnic ")
        try:
          c=int(input())
          if c==self.cnic:
              p=input("Enter a Password ")
              if p==self.password:
                  print(" Name ",self.name)
                  print("Last Name ",self.last_name)
                  print("Your balance are ",self.balance)
          else:
             print("No account found or incorrect cnic ")
        except ValueError as e:
            print("Expectin occure")
      else:
          print("Your account is Deactive \n No action will be done until \n You inactve the account")

    def blink_message(self, message):
        for _ in range(2): 
            sys.stdout.write("\r" + message)  
            sys.stdout.flush()  
            time.sleep(0.5)  
            sys.stdout.write("\r" + " " * len(message)) 
            sys.stdout.flush() 
            time.sleep(0.5)  
            
     
    def info(self):
              print("Here are your Account Information ")
              print("Account number ",self.account_number)
              print("Account Name ",self.name)
              print("Last name ",self.last_name)
              print("Created date ",self.created_date)
              print("Expire Date ",self.expire_date)
              print("Current Status ",self.status)
              print("Email ",self.email)
              print("Password ",self.email)
              print("Status type ",self.status)

