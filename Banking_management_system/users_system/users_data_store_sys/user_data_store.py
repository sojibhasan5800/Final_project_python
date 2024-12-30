#-------------Connection_System---------------
import os
import sys
import textwrap
from tabulate import tabulate
from datetime import datetime
from sys_needed_part.data_store.store import Account
class Bank_Store_manager:
    _account_list={} # key: account_id,value: cus_account_obj
    _bank_account_balance = 1000000
    _bank_transaction_history=[]
    _total_loan=0
    _loan_service = True
    _bankrupt_service = False

    def __init__(self,cus_name):
        self.__cus_name = cus_name
        self.__email=None
        self.__phone_number=None
        self.__Adress=None
        self.__account_id=None
        self.__acount_type = None
        self.__balance=0
        self.__loan_cnt=0
        self.transcation_history=[]

    def add_cus_store_info(self,user_cus_email,user_cus_Number,account_id,user_cus_adress,account_type):

        self.__email = user_cus_email
        self.__phone_number = user_cus_Number
        self.__Adress = user_cus_adress
        self.__account_id = account_id
        self.__acount_type = account_type
        Bank_Store_manager._account_list[account_id]=self
    
    def get_account_obj(self,account_number):
        if account_number in Bank_Store_manager._account_list.keys():
            return True, Bank_Store_manager._account_list[account_number]
        else:
            return False,False
    
    def deposite_ammount_account(self,amount):

        if (amount>0):
            self.__balance+=amount
            Bank_Store_manager._bank_account_balance+=amount
            history = (f"""Deposite Ammount '{amount}' tk for Account_Id: {self.__account_id} Successfully.
            Your available Balance is {self.__balance}""")
            his_lst = [history,datetime.now().strftime(" %H:%M:%S %Y-%m-%d"),"Deposite"]
            self.transcation_history.append(his_lst)
            Bank_Store_manager._bank_transaction_history.append(his_lst)
            print(history)

        else:
            print(f"Place Ammount given are More than 0 tk and try Again !!")
            
    def withdraw_ammount_account(self,amount):

        if(Bank_Store_manager._bankrupt_service == True):
            print(f" The bank is bankrupt !!")
            return
        
        if (self.__balance >= amount):
            self.__balance-=amount
            Bank_Store_manager._bank_account_balance-=amount
            history = (f"""Ammount '{amount}' tk withdraw Successfully for Account_Id :{self.__account_id}
            Your available Balance is {self.__balance}""")
            his_lst = [history,datetime.now().strftime(" %H:%M:%S %Y-%m-%d"),"Withdraw"]
            self.transcation_history.append(his_lst)
            Bank_Store_manager._bank_transaction_history.append(his_lst)
            print(history)

            
        else:
            print(f"“Withdrawal amount '{amount}' Tk exceeded” ")
    
    def get_balance(self):
        print(f"Account_Id: {self.__account_id} Balnce is '{self.__balance}' tk.")
    
    def get_transaction_history(self):

        if not self.transcation_history:
            print(f"Account_id : '{self.__account_id}' User Transaction Hisotry are Empty")
            return
        print(f"Account_Id: {self.__account_id} Transcation History below: ")
        headers = ["S.No","Type", "Details", "Date&Time"]
        table = []
        headers = [header.ljust(25) if header == "Type" else header for header in headers]
        for i, history in enumerate(self.transcation_history, start=1):
            details = history[0]
            date_time = history[1]
            transaction_type = history[2]
            wrapped_details = textwrap.fill(details, width=40)
            # table.append([i, transaction_type, details, date_time])
            table.append([i, transaction_type, wrapped_details, date_time])

        print(tabulate(table, headers=headers, tablefmt="fancy_grid", colalign=("center", "center", "center")))


    def take_loan_bank(self,amount):
       
        if(Bank_Store_manager._loan_service == False):
            print(f"Bank Authority Are Loan Service Off")
            return

        if(self.__loan_cnt >= 2):
            print(f"You have already 2(two) time take loan can not provided are more loan!!")
            return
        
        self.__loan_cnt+=1
        print(self.__loan_cnt)
        Bank_Store_manager._total_loan+=amount
        Bank_Store_manager._bank_account_balance-=amount
        self.__balance+=amount
        history = f"Dear '{self.__cus_name}' Loan '{amount}' tk Prospress Successfully"
        his_lst = [history,datetime.now().strftime(" %H:%M:%S %Y-%m-%d"),"Take_Loan"]
        self.transcation_history.append(his_lst)
        Bank_Store_manager._bank_transaction_history.append(his_lst)            
        print(history)
    
    def transaction_another_account(self,transaction_account_id,amount):
        # if transaction_account_id not in Bank_Store_manager._account_list.keys():
        #     print(f"“Account does not exist”.")
        if (self.__balance < amount):
            print(f"Your Account Balance Are Not Enough to Transfer Ammount '{amount}' tk")
        else:

            print()
            self.__balance-=amount
            Bank_Store_manager._bank_account_balance-=amount
            history = (f"""Transcation_id: {transaction_account_id} and Ammount '{amount}' tk Transfer Successfully.
            Your Avaiable Balance is '{self.__balance}' tk """)
            his_lst = [history,datetime.now().strftime(" %H:%M:%S %Y-%m-%d"),"Transaction"]
            self.transcation_history.append(his_lst)
            Bank_Store_manager._bank_transaction_history.append(his_lst)
            print(history)




#-------------- users_Service ---------------------------------
def user_create_account_obj(user_cus_name,user_cus_email,user_cus_Number,account_id,user_cus_adress,account_type):
    user_name_obj = Bank_Store_manager(user_cus_name)
    user_name_obj.add_cus_store_info(user_cus_email,user_cus_Number,account_id,user_cus_adress,account_type)
    Account._cus_store_obj[user_cus_email]=user_name_obj
def account_exit(account_number):
    return Bank_Store_manager.get_account_obj(None,account_number)



