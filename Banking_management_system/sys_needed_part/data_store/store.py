#-------------Connection_System-----------------------
import random 
#-----------Seller & Customer_Account Store-----------
       
class Account:
    _admin_account_stores={} # key : account_id ,key_value: name,email_id,number,password,user
    _customer_account_stores={} # key : account_id ,key_value: name,email_id,number,password,user
    __store_user_id=set() # value: unique user id
    _cus_store_obj={} #key : seller_email , value: customer_obj
    __admin_store_obj={} # key : customer_email, value : admin_obj
    
    

    def _generate_emp_id(self):
         """Generate a unique 4-digit ID."""
         while True:
             un_account_id = random.randint(100000,999999)
             if un_account_id not in Account.__store_user_id:
                 return un_account_id
    
    def customer_account_store(self,user_cus_name, user_cus_email,user_cus_Number,user_cus_Password,user,user_cus_adress,account_type):
                                                                        
          
          account_id = Account._generate_emp_id(None)
          if(account_type=="1"):
              account_type ="Saving Account"
          else:
              account_type ="Current Account"
              
          Account._customer_account_stores[account_id]={
           "Name": user_cus_name,
           "Email_id":user_cus_email,
           "Phone_Number":user_cus_Number,
           "Password":user_cus_Password,
           "User" : user,
           "User_Address":user_cus_adress,
           "Account_type":account_type

          }
          
          return account_id
    
    def get_customer_account_len(self):
        return len(Account._customer_account_stores)
    
    def admin_account_store(self,user_cus_name, user_cus_email,user_cus_Number,user_cus_Password,user,user_cus_adress,branch_code):

                                                                     
          account_id = Account._generate_emp_id(None)
          Account._admin_account_stores[account_id]={
           "Name": user_cus_name,
           "Email_id":user_cus_email,
           "Phone_Number":user_cus_Number,
           "Password":user_cus_Password,
           "User" : user,
           "User_Address":user_cus_adress,
           "Branch_Code":branch_code

          }
          return account_id
    
    #Add shop_sotre_obj
    def seller_shop_obj_store(self,user_cus_email:str,shop_obj):
        Account.__shop_store_obj[user_cus_email]=shop_obj
   
   #Add_customer_store_obj
    def customer_obj_store(self,user_cus_email:str,cus_obj):
        Account.__customer_store_obj[user_cus_email]=cus_obj
    
    def mail_matching(self,user_cus_email,user_cus_password):
         
         for user_id, details in Account._customer_account_stores.items():
            if details["Email_id"] == user_cus_email and details["Password"] == user_cus_password:
                if(details["User"]=="Seller"):
                    return True,user_id,details["User"],Account.__shop_store_obj[user_cus_email]
                else:
                    return True,user_id,details["User"],Account.__customer_store_obj[user_cus_email]
            else:
                return False,False,False,False
    
    def duplicated_mail_checking(self,user_cus_mail,users):
        if(users=="Customer"):
            if user_cus_mail in Account._cus_store_obj.keys():
                return False
        return True
    
    def get_admin_len(self):
        if (len(Account._admin_account_stores) <=1):
            return True
        else:
            return False
    
#---------- Adnmin_account_service---------
def admin_account_len():
    return Account.get_admin_len(None)
def admin_person_eixt():
    return len(Account._admin_account_stores)





         
         
         
          
            
