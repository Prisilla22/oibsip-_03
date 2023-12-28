import random

ch="1234567890qwertyuiopasdfghjklzxcvbnmASDFGHJKLZXCVBNMQWERTYUIOP~!@#$%^&*.,/-=+"

def ran_pass():
    while True:
        pass_len=int(input("Enter the length of the password You Want: "))
        password = ""
        for x in range(0,pass_len):
            password_ch = random.choice(ch)
            password = password + password_ch
        print("Your Password : ", password)
        break
        

ran_pass()
i=int(input("Do you want more passwords: (1 for yes)  (2 for No): "))
if(i == 1):
    c=int(input("How many more passwords do you want: "))
    for x in range(0,c):
        ran_pass()
    print("-----Hope the passwords given is useful and strong-----")
else:
    print("-----Hope the password given is useful and strong-----")
    exit()