from _ast import Or
f = open(r"C:\Users\User\Desktop\AOC\input\Day2.txt")

isValidI = 0
isValidII = 0

for line in f:    
    # parsing password policy and password
    step0 = line.split(' ')  
    
    # parsing range 
    step1 = step0[0].split('-')   
    low = int(step1[0])
    high = int(step1[1])
    
    # parsing given letter
    step2 = step0[1].split(':')
    given_letter = step2[0]
    
    # password
    password = step0[2]
    
    # PART I   
    given_letter_count = 0
    for ch in password:
        if ch == given_letter:
            given_letter_count += 1

    if given_letter_count >= low and given_letter_count <= high:
        isValidI += 1
        

    # PART II
    if (password[low-1] == given_letter and password[high-1] != given_letter) or (password[low-1] != given_letter and password[high-1] == given_letter):
        isValidII += 1       

 
  
print("PART I Answer")      
print(isValidI)

print("PART II Answer")
print(isValidII)
