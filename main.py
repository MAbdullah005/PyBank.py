
customer1=Customer()
customer1.enter_info()
customer2=Customer()
customer2.enter_info()
HBLpkL12=Bank("HBl Bank","Lahore","pakistan","23sxs","hbl121@gmail.com")
account1=HBLpkL12.Create_account(customer1)
account2=HBLpkL12.Create_account(customer1)
HBLpkL12.Trnasfer(account1,account2,100)
account2.Check_balance()
HBLpkL12.Accounts_details()
HBLpkK11=Bank("hbl Bank","Karachi","pakistan","23sxs","bubl21@gmail.com")
customer3=Customer()
customer3.enter_info()
customer4=Customer()
customer3.enter_info()
HBLpkL12=Bank("HBl Bank","Lahore","pakistan","23sxs","hbl121@gmail.com")
account1=HBLpkL12.Create_account(customer3)
account2=HBLpkL12.Create_account(customer4)
HBLpkL12.Trnasfer(account1,account2,100)
account2.Check_balance()
HBLpkL12.Accounts_details()
