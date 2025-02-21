class Bank: 
    
    def __init__(self,bankname,location,city,code,bank_mail):
        self.bank_name=bankname
        self.accounts=[]
        self.Loaction=location
        self.balance=int
        self.City=city
        self.code=code
        self.bank_mail=bank_mail
        self.status=bool

        # Deposit money into bank


    def Create_account(self,person)->Account:
       new_accout=Account(person.cnic)
       new_accout.Create_account()
       self.accounts.append(new_accout)
       return new_accout

    def Accounts_details(self):
        print("Here are the All account detail thats is login to Bank ")
        file_path='D:\python.pyt\PythonApplication1\PythonApplication1\Bank Accounts.csv'
        for account in self.accounts:
            print(account,"done")
            print("\tAccount number ",a," information")
            Account.info(account)
            a=a+1
        with sqlite3.connect("DataBase.db") as conn:
            command="SELECT * FROM DATA"
            cursor=conn.execute(command)
            header = ['ID', 'First Name', 'Last Name', 'Phone', 'Start Date', 'End Date', 'Email', 'Password', 'Account ID']
            self.Write_data(header,cursor)
            self.Read_data()
            self.open_file_in_default_application(file_path)
    def Read_data(self):
        with open("Bank Accounts.csv",mode='r') as file:
                 reader=csv.reader(file)
                 header=next(reader)
                 print("Header",header)
                 for row in reader:
                     print(row)
    def Write_data(self,header,rows):
        with open('Bank Accounts.csv', mode='w', newline='') as file:
               writer = csv.writer(file)
               writer.writerow(header)
               writer.writerows(rows)

    def open_file_in_default_application(self,file_path):
      if platform.system() == "Windows":
        # Open with the default program (Excel, WPS, etc.)
        os.startfile(file_path)
      elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", file_path])
      elif platform.system() == "Linux":
        subprocess.run(["xdg-open", file_path])


    def Trnasfer(self,from_acount,to_account,amouth):
         if from_acount not in self.accounts and to_account not in self.accounts:
             print("Account not exist in bank enter a proper account ")
             return 
         if from_acount.balance<0:
             print("Insufficant fund")
             return
         from_acount.balance-=amouth
         to_account.balance+=amouth
         print(f"Transferred ${amouth} from {from_acount.account_number} to {to_account.account_number}")
