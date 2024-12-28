import os
import sys
sys.path.append(r"Banking\Final_project_python\Banking_management_system")
from sys_needed_part.valid_check_sys.valid_data import Cheking_User_data

#---------customer_dispaly_Entry-----------------
customer_dis_list=[]
customer_dis_list.append(" (1) Deposite Amount Enter                                    : ")
customer_dis_list.append(" (2) Withdraw Amount Enter                                    : ")
customer_dis_list.append(" (3) Check Available Balance Enter                            : ")
customer_dis_list.append(" (4) Check Transaction History Enter                          : ")
customer_dis_list.append(" (5) Can Take a Loan From The Bank('at most two times') Enter : ")
customer_dis_list.append(" (6) Trnasfer Another Account Enter                           : ")
customer_dis_list.append(" (7) Back Main Menu                                           : ")
customer_dis_list.append(" (8) Exit Enter                                               : ")

#----------customer_display_fun------------------
def customer_display_menu():
    for view_menu_customer_dis_list in customer_dis_list:
        print(view_menu_customer_dis_list)


#-------------------------customer Display Data given---------------------
def customer_service_display_data(account_obj):
    while True:
        print()
        customer_display_menu()
        x = input()
        if(Cheking_User_data(x,"Customer_inner_page")):
            x = int(x)
            if(x==1):
                # ---------Deposite Amount Enter-----------
                print(f"Enter the Deposite Ammount: ")
                try:
                    amount = int(input())
                    account_obj.deposite_ammount_account(amount)
                except Exception as e:
                    print(f"{e} : Place Deposite Ammount Only Digit!!")
                    continue

            elif(x==2):
                #---------- Withdraw Amount Enter --------------------
                print(f"Enter the Withdraw Ammount: ")
                try:
                    amount = int(input())
                    account_obj.withdraw_ammount_account(amount)
                except Exception as e:
                    print(f"{e} : Place Deposite Ammount Only Digit!!")
                    continue
                
            elif(x==3):
                #------------Check Available Balance----------
                account_obj.get_balance()
            elif(x==4):
                #------------Check Transaction History----------
                account_obj.get_transaction_history()
            elif(x==5):
                #------------Can Take a Loan From The Bank----------
                print(f"Enter the Taken Loan Ammount: ")
                try:
                    amount = int(input())
                    account_obj.take_loan_bank(amount)
                except Exception as e:
                    print(f"{e} : Place Deposite Ammount Only Digit!!")
                    continue  
            elif(x==6):
                #------------Trnasfer Another Account----------
                try:
                    print(f"Enter the Transfer Account Number: ")
                    account_number = int(input())
                    print(f"Enter the Transfer Ammount: ")
                    amount = int(input())
                    account_obj.transaction_another_account(amount)
                except Exception as e:
                    print(f"{e} : Place Given Only Digit!!")
                    continue
            elif(x==3):
                #------------Back_return_main_page----------
                return "customer_main_page"  
            elif(x==8):
                #-----------Exit_Programme------------
                print("Exiting system. Goodbye!")
                print(f"-----------------------")
                return 
                
                
            
        else:
            #--------again_run_program
            continue


