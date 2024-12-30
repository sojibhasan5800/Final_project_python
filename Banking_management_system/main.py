#-------------Connection_System---------------
import re
import os
import sys
# sys.path.append(r"Banking\Final_project_python\Banking_management_system")

from sys_needed_part.valid_check_sys.valid_data import Cheking_User_data,inside_checking
# from users_system.user import customer_display_data
from users_system.user import customer_display_data
from admin_system.admin import admin_display_data
from sys_needed_part.Registration_from.reg import reg_display_from,login_display_from
from sys_needed_part.data_store.store import admin_account_len,admin_person_eixt

#---------Users_dispaly_Entry-----------------
main_lst=[]
main_lst.append(" (1) User  Services  Press              : ")
main_lst.append(" (2) Admin Services  Press              : ")
main_lst.append(" (3) Admin Registration Account   Press : ")
main_lst.append(" (4) Exit  Program  Press               : ")

#----------Users_display_fun------------------
def user_display_menu():
    for view_menu_user_dis_list in main_lst:
        print(view_menu_user_dis_list)

#-------------------------Users Display Data given---------------------

while True:
    print()
    user_display_menu()
    x = input()
    if(Cheking_User_data(x,"Registration")):
        x = int(x)
        if(x==1):
            #-----------User  Services-----------
            action_main_page = customer_display_data()
            if(action_main_page == "main_page"):
                continue
            elif(action_main_page =="system_exit"):
                break

        elif(x==2):
            #----------- Admin Services -----------
            result,admin_name,admin_obj = login_display_from()
            if(result):
                action_main_page = admin_display_data(admin_obj)
                if(action_main_page == "main_page"):
                    continue
                elif(action_main_page =="system_exit"):
                    break
           
            
            
        elif(x==3):
            #----------- Admin Registration Account-----------
            if( admin_person_eixt()):
                print("Admin Are Already Exit Place Login Admin serivce !!")
            else:
                while True:
                    result,account_id,user_cus_name =reg_display_from("Admin")
                    if(result):
                        print(f"Dear {user_cus_name} Admin Account Create is Successfully")
                        print(f"Your Account Id: {account_id}")
                        break
                    else:
                        if(inside_checking("Account_create")):
                            continue
                        else:
                            break

            
        elif(x==4):
            #-----------Exit_Programme------------
            print("Exiting system. Goodbye!")
            print(f"-----------------------")
            break
    else:
        #--------again_run_program
        continue






