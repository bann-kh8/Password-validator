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


# input a password contain: 1 upper case, 1 sympol and its length 8 or more
# my code 
password=input("enter a password: ")
upper=0
sympol=0
lower_num=0
if len(password) >=8 :
    for chr in password:
        if chr.isspace(): 
            break
            if chr.isupper():
                upper+=1
            if chr.isalnum():
                lower_num+=1
            else:
                sympol+=1
                
        
    if upper==1 and sympol==1:
        print("valid password")
    else:
        print("invalid password")                
                
else:
    print("invalid password  # ")  




"""









                 
"""


from random import randint

def password_length(length):
   global password
   for i in range (length-2):
       password=password+randomCharacter("abcdefghijklmnopqrstuvwxyz")

def digit():
    global password
    password=password+str(randint(0,9))
    
def sympols():
    global password
    password=password+randomCharacter("@#$%&*()+/\!")  
    
def upper ():
    global password
    password=password+randomCharacter("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
     
def randomCharacter(chr):
    global password
    length=len(chr)
    return chr[randint(0,length-1)]
    

def main ():
    password_length(8) 
    digit()
    sympols()
    upper()       
password=""    
main()    
print(password)

"""