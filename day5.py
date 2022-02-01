import random
import sys
alphabet = 'qwertyuiopasdfghjklzxcvbnm' + '!@#$%^&*()\\/,.-_~`' + 'qwertyuiopasdfghjklzxcvbnm'.upper()
password = ''
for n in range(1, int(sys.argv[1])+1):
    password += random.choice(alphabet)
print(password)