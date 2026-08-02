# input a password contain: 1 upper case, 1 sympol and its length 8 or more
# improved after asking the  doctor 
# 
password=input("enter a password: ")
upper=0
sympol=0
lower_num=0
if len(password) >=8 and " " not in password:
    for chr in password:
            if chr.isupper():
                upper+=1
            elif chr.isdigit() and chr.islower():
                lower_num+=1
            else:
                sympol+=1
                
        
    if upper==1 and sympol==1:
        print("valid password")
    else:
        print("invalid password")                
                
else:
    print("invalid password  # ")  











 
