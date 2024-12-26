#-------------Connection_System---------------
import re
import os
import sys
import pyautogui
import time
sys.path.append(r"Shoping_managment_system")


#------Regestration_From---------
def reg_display_from(user):
    
   #  if(user=="Seller"):
   #     time.sleep(3)
   #     print("Enter Your Shop Name: ")
   #     shope_name = str(input()).strip()
   #     shope_name=re.sub(r'\s{2,}',' ',shope_name)

   #  print("Enter First Name : ")
   #  first_name = str(input()).strip()
   #  print("Enter Last  Name : ")
   #  last_name = str(input()).strip()
   #  user_cus_name ="".join((first_name + " "+ last_name))
   #  user_cus_name=re.sub(r'\s{2,}',' ',user_cus_name)

   #  print("Enter Phone Number  : ")
   #  user_cus_Number = str(input()).strip()

   #  print("Enter Email  Id  : ")
   #  user_cus_email = str(input()).strip()  

   #  print("Create a strong password: ")
   #  user_cus_Password = str(input()).strip()
   #  print("Retype your password: ")
   #  user_retype_cus_password = str(input()).strip()
     def auto_complete_input(prompt, example_input):
        print(prompt)
        time.sleep(1)  # Simulate delay
        print(example_input)  # Display example input
        return example_input  # Return auto-filled input

     if user == "Seller":
         shope_name = auto_complete_input("Enter Your Shop Name:", "Test Shop")
         shope_name = re.sub(r'\s{2,}', ' ', shope_name)

     first_name = auto_complete_input("Enter First Name:", "John")
     last_name = auto_complete_input("Enter Last Name:", "Doe")
     user_cus_name = " ".join((first_name, last_name))
     user_cus_name = re.sub(r'\s{2,}', ' ', user_cus_name)  
     user_cus_Number = auto_complete_input("Enter Phone Number:", "01623966595")
     user_cus_email = auto_complete_input("Enter Email Id:", "john.doe@example.com")
     user_cus_Password = auto_complete_input("Create a strong password:", "@StrongPass123")
     user_retype_cus_password = auto_complete_input("Retype your password:", "@StrongPass123")

     result = user_data_check(user_cus_name,user_cus_email,user_cus_Number,user_cus_Password,user_retype_cus_password)
     
     user_id= None
     if(result):
        if(Account.duplicated_mail_checking(None,user_cus_email,user)==False):
           return False,False,False
        user_id = Account.customer_seller_account_store(None,user_cus_name,user_cus_email,user_cus_Number,user_cus_Password,user)
        if(user == "Seller"):
           shop_id = user_id
           shop_obj = create_shop(shope_name,shop_id)
           Account.seller_shop_obj_store(None,user_cus_email,shop_obj)
        elif(user=="Customer"):
           cus_id = user_id
           cus_obj = create_customer(user_cus_name,cus_id)
           Account.customer_obj_store(None,user_cus_email,cus_obj)
           
     return result,user_id,user_cus_name

#-------Login_From---------
def login_display_from():
  print("Enter Email  Id  : ")
  user_cus_email = str(input()).strip()  

  print("Create a strong password: ")
  user_cus_Password = str(input()).strip()

  result ,user_id,users,user_obj= Account.mail_matching(None,user_cus_email,user_cus_Password)
  return result ,user_id,users,user_obj

     
  


