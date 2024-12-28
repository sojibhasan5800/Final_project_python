#-------------Connection_System---------------
import os
import sys
from tabulate import tabulate
sys.path.append(r"Banking\Final_project_python\Banking_management_system\sys_needed_part")
from users_system.users_data_store_sys.user_data_store import Bank_Store_manager
from sys_needed_part.data_store.store import Account
class Admin_Store_manager:
    __admin_account_list={} # key: account_id,value: cus_account_obj
    

    def __init__(self,admin_name):
        self.__admin_name = admin_name
        self.__email=None
        self.__phone_number=None
        self.__Adress=None
        self.__account_id=None
        self.__user = None
        self.__branch_code = None
        
        

 
    #Store Info add:
    def add_admin_store_info(self,user_cus_email,user_cus_Number,account_id,user_cus_adress,user,branch_code):

        self.__email = user_cus_email
        self.__phone_number = user_cus_Number
        self.__Adress = user_cus_adress
        self.__user = user
        self.__account_id = account_id
        self.__branch_code = branch_code
        Admin_Store_manager.__admin_account_list[account_id]=self
    
    #Get Account_obj
    def get_account_obj(self,account_number):
        return Admin_Store_manager.__admin_account_list[account_number]
    
    def user_account_delete(self,delete_account_id):
        if delete_account_id not in Bank_Store_manager.__account_list.keys():
            print(f"This deleted Account Number '{delete_account_id}' do not Exit! Place Try Again")
        else:
            del Bank_Store_manager.__account_list[delete_account_id]
            del Account.__customer_account_store[delete_account_id]
            print(f"Acccount_Id : '{delete_account_id}' Removed Successfully")

    def customer_total_account_lst_bank(self):

        headers = ["Account ID", "Name", "Email ID", "Phone Number", "Password", "User", "User Address", "Account Type"]
        table = []
        for account_id, data in Account.__customer_account_store.items():

            # Mask the password with asterisks
            masked_password = '*' * len(data["Password"])
            
            # Add the row to the table with the masked password
            table.append([
                account_id,
                data["Name"],
                data["Email_id"],
                data["Phone_Number"],
                masked_password,
                data["User"],
                data["User_Address"],
                data["Account_type"]
            ])
        
        # Display the data in tabular format
        print(tabulate(table, headers=headers, tablefmt="fancy_grid", colalign=("center", "center", "center")))

    def get_total_balance_bank(self):
        print(f"Our Bank Total Amount is :'{Bank_Store_manager.__bank_account_balance}' tk.")

    def get_show_loan_bank(self):
        print(f"Our Bank Total Loan Given is :'{Bank_Store_manager.___total_loan}' tk.")

    def checkout_loan_service(self,on_off):
        if(on_off=="1"):
            Bank_Store_manager.__loan_service = True
            print("Loan Service On Successfully")
        elif(on_off=="0"):
            Bank_Store_manager.__loan_service = False
            print("Loan Service On Successfully")
        




  

#-------------- Admin_Service ---------------------------------
def create_admin_obj(user_cus_name,user_cus_email,user_cus_Number,admin_account_id,user,user_cus_adress,branch_code):
    admin_obj = Admin_Store_manager(user_cus_name)
    admin_obj.add_admin_store_info(user_cus_email,user_cus_Number,admin_account_id,user_cus_adress,user,branch_code)

def admin_account_exit(account_number):
    return Admin_Store_manager.get_account_obj(None,account_number)