#-------------Connection_System---------------
import re
import os
import sys
import pyautogui
import time

# sys.path.append(r"Final_project_python\Banking_management_system\sys_needed_part")
# sys.path.append(r"Final_project_python\Banking_management_system")
from sys_needed_part.valid_check_sys.valid_data import user_data_check
from sys_needed_part.data_store.store import Account,admin_account_len,admin_person_eixt

from users_system.users_data_store_sys.user_data_store import user_create_account_obj
from admin_system.admin_data_stores_sys.admin_data_store import create_admin_obj,admin_account_exit
#------Regestration_From---------
def reg_display_from(user):

   if(user=="Admin"):
      if(not admin_account_len()):
         print("Admin Are Only One Already Exit Place Login Sir!!")
         return False,False,False
      
    
   if(user=="Admin"):   
      print("Enter Bank Branch Code(int): ")
      branch_code = str(input()).strip()
      branch_code=re.sub(r'\s{2,}',' ',branch_code)
      print("Enter Admin First Name : ")
      first_name = str(input()).strip()
      print("Enter Admin Last  Name : ")
      last_name = str(input()).strip()
      user_cus_name =first_name + " "+ last_name
      user_cus_name=re.sub(r'\s{2,}',' ',user_cus_name)
      print("Enter Your Adress : ")
      user_cus_adress = str(input()).strip()
      print("Enter Phone Number  : ")
      user_cus_Number = str(input()).strip()
      print("Enter Email  Id  : ")
      user_cus_email = str(input()).strip()  
      print("Create a strong password: ")
      user_cus_Password = str(input()).strip()
      print("Retype your password: ")
      user_retype_cus_password = str(input()).strip()

      # branch_code = "101" # Example branch code
      # first_name = "John"
      # last_name = "Doe"
      # user_cus_name = re.sub(r'\s{2,}', ' ', f"{first_name} {last_name}")
      # user_cus_adress = "123 Main Street, Springfield"
      # user_cus_Number = "01623966595"
      # user_cus_email = "john.doe@example.com"
      # user_cus_Password = "StrongPassword123@"
      # user_retype_cus_password = "StrongPassword123@"

   elif(user=="Customer"):

      print("Enter User's First Name : ")
      first_name = str(input()).strip()
      print("Enter User's Last  Name : ")
      last_name = str(input()).strip()
      user_cus_name =first_name + " "+ last_name
      user_cus_name=re.sub(r'\s{2,}',' ',user_cus_name)
      print("Enter Your Adress : ")
      user_cus_adress = str(input()).strip()
      print("Enter Phone Number  : ")
      user_cus_Number = str(input()).strip()
      print("Enter Email  Id  : ")
      user_cus_email = str(input()).strip()  
      print("Create a strong password: ")
      user_cus_Password = str(input()).strip()
      print("Retype your password: ")
      user_retype_cus_password = str(input()).strip()
      print("Enter Choice Account Type : ")
      print("(1) Svaing Account  (2) Current Account")
      account_type = str(input())
      
      # account_type = "1" # Example branch code
      # first_name = "abol"
      # last_name = "Doe"
      # user_cus_name = re.sub(r'\s{2,}', ' ', f"{first_name} {last_name}")
      # user_cus_adress = "123 Main Street, Springfield"
      # user_cus_Number = "01623966595"
      # user_cus_email = "john.doe@example.com"
      # user_cus_Password = "StrongPassword123@"
      # user_retype_cus_password = "StrongPassword123@"


 
   if(user=="Admin"):
      result = user_data_check(user,branch_code,user_cus_name,user_cus_email,user_cus_Number,user_cus_Password,user_retype_cus_password)
   elif(user=="Customer"):
      result = user_data_check(user,account_type,user_cus_name,user_cus_email,user_cus_Number,user_cus_Password,user_retype_cus_password)
   
   
   account_id= None
   if(result):
      if(user=="Admin"):
         account_id = Account.admin_account_store(None,user_cus_name,user_cus_email,user_cus_Number,user_cus_Password,user,user_cus_adress,branch_code)
         create_admin_obj(user_cus_name,user_cus_email,user_cus_Number,account_id,user,user_cus_adress,branch_code)
         return True,account_id,user_cus_name
      elif(user=="Customer"):
         if(Account.duplicated_mail_checking(None,user_cus_email,user)==False):
            print(f"This Email '{user_cus_email}' are Already Used Place Another Email")
            return False,False,False
         
         account_id = Account.customer_account_store(None,user_cus_name,user_cus_email,user_cus_Number,user_cus_Password,user,user_cus_adress,account_type)
         user_create_account_obj(user_cus_name,user_cus_email,user_cus_Number,account_id,user_cus_adress,account_type)
         return True,account_id,user_cus_name
   else:
      print()
      return False,False,False    
   
  
         
 
#-------Login_From---------
def login_display_from():
   if(admin_person_eixt()==0):
      print("Place Regrestation Admin Account Than Login Service !!!")
      return False,False,False
   try:
         
      print("Enter Bank Branch Code : ")
      branch_code = (input())

      print("Enter The Account Id Number : ")
      account_id = int(input())

      print("Enter Your Password : ")
      admin_password = str(input().strip())

      # branch_code ="101"
      # admin_password="StrongPassword123@"
      

      
   except Exception as e:
         
      print(f"Exception: Something went wrong with the input. Error: {e} Place Try again!!")
      return False,False,False
   
   if account_id not in Account._admin_account_stores.keys():
      print(f"This account id: {account_id} do not matching Admin Account !!")
      return False,False,False
   if(Account._admin_account_stores[account_id]["Branch_Code"] != branch_code):
      print(f"This branch '{branch_code}' Code are Wrong !!")
      return False,False,False
   if(Account._admin_account_stores[account_id]["Password"] != admin_password):
      print(f"This branch '{branch_code}' Code are Wrong !!")
      return False,False,False
   obj = admin_account_exit(account_id)
   admin_name = Account._admin_account_stores[account_id]["Name"]
   return True,admin_name,obj
   
  
      

     
     
  
 

#   result ,user_id,users,user_obj= Account.mail_matching(None,user_cus_email,user_cus_Password)
#   return result ,user_id,users,user_obj

     
  


