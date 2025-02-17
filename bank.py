
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

          self.status=True
      print("Here are your account number ",self.account_number)
      print("Your account status is active",self.status)
