import os
import sys
sys.path.append(r"Banking\Final_project_python\Banking_management_system")
from sys_needed_part.valid_check_sys.valid_data import Cheking_User_data,inside_checking
from sys_needed_part.Registration_from.reg import reg_display_from
from users_data_store_sys.user_data_store import account_exit
from users_service_sys.user_service import customer_service_display_data
#---------customer_dispaly_Entry-----------------
customer_dis_list=[]
customer_dis_list.append(" (1) Create An User's Account  Enter                     : ")
customer_dis_list.append(" (2) Provide an account ID to access your service Enter  : ")
customer_dis_list.append(" (3) Back Main Menu                                      : ")
customer_dis_list.append(" (4) Exit Enter                                          : ")

#----------customer_display_fun------------------
def customer_display_menu():
    for view_menu_customer_dis_list in customer_dis_list:
        print(view_menu_customer_dis_list)


#-------------------------customer Display Data given---------------------
def customer_display_data():
    while True:
        print()
        customer_display_menu()
        x = input()
        if(Cheking_User_data(x,"Customer_main_page")):
            x = int(x)
            if(x==1):

                # ---------Create An Account-----------
                while True:
                    result,account_id,user_cus_name =reg_display_from("Customer")
                    if(result):
                        print(f"Dear {user_cus_name} Account Create is Successfully")
                        print(f"Your Account Id: {account_id}")
                        break
                    else:
                        if(inside_checking("Account_create")):
                            continue
                        else:
                            break

            elif(x==2):
                #---------- Account Access --------------------
                try:
                    print("Enter Your Account Number : ")
                    account_number = int(input())
                    result,account_obj = account_exit(account_number)
                except Exception as e:
                    print(f"Your Account Number '{account_number}' Invalid Place Only Digit Provided !!")
                    continue
                
                if(result):
                   action = customer_service_display_data(account_obj)
                   if(action =="customer_main_page"):
                       continue
                   elif(action == "system_exit"):
                       return "system_exit"
                else:
                    print(f"This Account_id '{account_number}' are Invalid !!!!!!!")
                    continue
                
            elif(x==3):
                #------------Back_return_main_page----------
                return "main_page"
                
            elif(x==4):
                #-----------Exit_Programme------------
                print("Exiting system. Goodbye!")
                print(f"-----------------------")
                return "system_exit"
                
            
        else:
            #--------again_run_program
            continue


