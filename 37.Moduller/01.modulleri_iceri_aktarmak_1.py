## Modüller

## 01_Modülleri İçeri Aktarmak

import os
##print(dir(os))

print(os.name)

##if os.name == 'nt':
##    print('Windows tayız')
##else:
##    print('Linux veya Mac OS tayız')

print(os.getcwd())

try:
    os.makedirs('örnek_dizin')
except FileExistsError:
    print("örnek_dizin adında bir klasör zaten var!!")
