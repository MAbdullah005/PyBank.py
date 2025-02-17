
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
