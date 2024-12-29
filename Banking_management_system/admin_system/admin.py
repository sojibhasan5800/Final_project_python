import os
import sys

from sys_needed_part.valid_check_sys.valid_data import Cheking_User_data,inside_checking
from sys_needed_part.Registration_from.reg import reg_display_from
#---------admin_dispaly_Entry-----------------
admin_dis_list=[]
admin_dis_list.append(" (1) Create An Account  Enter                            : ")
admin_dis_list.append(" (2) Delete Any User Account Enter                       : ")
admin_dis_list.append(" (3) See All User Accounts List   Enter                  : ")
admin_dis_list.append(" (4) Check The Total Available Balance Of The Bank Enter : ")
admin_dis_list.append(" (5) Check The Total Loan Amount Enter                   : ")
admin_dis_list.append(" (6) On or Off The Loan Feature Of The Bank Enter        : ")
admin_dis_list.append(" (7) Back Main Menu                                      : ")
admin_dis_list.append(" (8) Exit Enter                                          : ")

#----------admin_display_fun------------------
def admin_display_menu():
    for view_menu_admin_dis_list in admin_dis_list:
        print(view_menu_admin_dis_list)


#-------------------------Admin Display Data given---------------------
def admin_display_data(admin_obj):
    while True:
        print()
        admin_display_menu()
        x = input()
        if(Cheking_User_data(x,"Admin")):
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

                #---------- Delete Any User Account--------------------
                try:
                    print("Enter the Deleted Account Id : ")
                    account_number = int(input())
                    admin_obj.user_account_delete(account_number)
                except Exception as e:
                    print(f"{e} Place Given Only Digit !!")

                
            elif(x==3):
                #---------- See All User Accounts List -------------------
                admin_obj.customer_total_account_lst_bank()

            elif(x==4):
                #----------Our_store_delete_item--------------------
                admin_obj.get_total_balance_bank()
            elif(x==5):

                #-----------Check The Total Loan Amount----------
                admin_obj.get_show_loan_bank()
            elif(x==6):

                #-----------On or Off The Loan Feature Of The Bank----------
                try:
                    
                    print("On The Loan  Service  Press (1) : ")
                    print("Off The Loan Service  Press (0) : ")
                    on_off = int( input())
                    if( (on_off>=0 and on_off<=1)):
                        admin_obj.checkout_loan_service(on_off)
                    else:
                        print(f"Invalid Number '{on_off}' Choice (1 or 2) Place try Again!!")
                except Exception as e:
                    print("Place Given (1 or 2) digit !!")
                    continue

            elif(x==7):
                #------------Back_return_main_page----------
                return "main_page"
                
            elif(x==8):
                #-----------Exit_Programme------------
                print("Exiting system. Goodbye!")
                print(f"-----------------------")
                return "system_exit"
                
            
        else:
            #--------again_run_program
            continue


