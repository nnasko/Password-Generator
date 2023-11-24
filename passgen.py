import random
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m' 

password =  []

for i in range(4):
    i = chr(random.randint(65,90))
    password.append(i)
for i in range(3):
    i = chr(random.randint(97,122)) 
    password.append(i)
for i in range(3):
    i = chr(random.randint(48,57))
    password.append(i)
for i in range(2):
    i = chr(random.randint(33,64))
    password.append(i)

random.shuffle(password)
password = ''.join(password)

os.system('cls' if os.name == 'nt' else 'clear')
print(f"{bcolors.OKCYAN}[OK] {bcolors.RESET}Your randomly generated password is:{bcolors.WARNING}{bcolors.BOLD} {password} {bcolors.RESET}")
