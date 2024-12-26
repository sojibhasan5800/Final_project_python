
#----------------------Checking_Valid_Promot_Data------------------------
def Cheking_User_data(x,users):
    if  x.isalpha():
        print(f"This {x} is alpha Character Place given integer Number !")
        return False
    elif x.isdigit():
        x = int(x)
        if ( users=="Registration" and ( x<1 or x>4)  ):
            print(f"Place Sir given This Number (1 to 4) are inclusive")
            return False
        elif(users=="Admin" and ( x<1 or x>7) ):
            print(f"Place Sir given This Number (1 to 7) are inclusive")
            return False
        elif(users=="Customer" and ( x<1 or x>8) ):
            print(f"Place Sir given This Number (1 to 8) are inclusive")
            return False
        elif(users=="Seller_exchange" and ( x<1 or x>3) ):
            print(f"Place Sir given This Number (1 to 3) are inclusive")
            return False
        elif(users=="Customer_exchange" and ( x<1 or x>4) ):
            print(f"Place Sir given This Number (1 to 4) are inclusive")
            return False
        else:
            return True
    else:
        print(f"This {x} is Numeric number Place given integer Number !")
        return False

#----------------------Checking_Valid_User_Information------------------------

#Checking_Valid_Email
import re
def is_valid_mail(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

#Checking_Valid_Name
def is_valid_name(user_name):

    username_pattern = r'^[a-zA-Z][a-zA-Z\s]{3,29}$'
    return re.match(username_pattern, user_name) is not None

#Checking_Valid_Number
import phonenumbers
def validate_and_format_number(number,default_code="BD"):
    try:
        parse_number = phonenumbers.parse(number,default_code)
        if phonenumbers.is_valid_number(parse_number):
            formatted_number = phonenumbers.format_number(parse_number,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            return formatted_number
        else:
         return False
    except phonenumbers.NumberParseException:
        return False

#Checking_Strong_Password
def is_strong_password(password):
    """Check if the password is strong (minimum 8 characters, includes uppercase, lowercase, number, and special character)."""
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&><])[A-Za-z\d@$!%*?&><]{8,30}$'
    return re.match(pattern, password) is not None
       

def user_data_check(user_name:str,user_email:str,user_Number:str,user_password:str,user_retype_password:str):
    invalid_list=[]
    if not (is_valid_mail(user_email)):
        invalid_mail = f"This Mail {user_email} is invalid"
        invalid_list.append(invalid_mail)

    if not (is_valid_name(user_name)):
         invalid_name = f"This Name '{user_name}' is Invalid"
         invalid_extra = f"Name Must be Only (4 to 30) Character Between"
         invalid_list.append(invalid_name)
         invalid_list.append(invalid_extra)

    if not(validate_and_format_number(user_Number)):
        invalid_number = f"This number '{user_Number}' is Invalid"
        invalid_list.append(invalid_number)

    if not (is_strong_password(user_password)):
         invalid_name  = f"This Password '{user_password}' is Invalid"
         invalid_extra = f"Password must be at least 8 characters long, include uppercase, lowercase, a number, and a special character, and must not exceed 30 characters."
         invalid_list.append(invalid_name)
         invalid_list.append(invalid_extra)
    
    if not (user_password == user_retype_password):
        invalid_match_pass = f"Passwords '{len(user_password)*'*'}'do not match. Please try again."
        invalid_list.append(invalid_match_pass)
    
    if(len(invalid_list)):
        for invalid_item in invalid_list:
            print(invalid_item)
        return False
    else:
        return True

#---------------Checking_inside_input_comment----------------

def inside_checking(users_check="Admin"):
     if(users_check=="Again_add_card"):
         print("If you more Items Added In Card Press (1) :")
         print("If you not  Items Added In Card Press (0) :")
     elif(users_check=="Invalid_promt"):
         print("If you again Added Item  press     (1): ")
         print("If you  Not again Added Item press (0): ")
     elif(users_check=="cus_Amount"):
         print("If you again Added Amount  press     (1): ")
         print("Otherwise you exit then Press        (0) :")
     elif(users_check=="Admin"):
         print("If you again input add  Press (1) :")
         print("Otherwise you exit then Press (0) :")
           
     again_input = input()
     if(again_input=="1"):
         return True
     else:
         return False
    