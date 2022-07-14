import os
import re
user = input('Please enter the dictionary path:')
def config():
    path="{}".format(user)
    if os.path.exists(path):
        print('[+]Dictionary file existence')
        print(user)
    else:
        print('[-]The target dictionary does not exist')
        exit()
def replace():
    path=user
    foropen=open(path,'r')
    wlcw=""
    for line in foropen:
        if re.search("/",line):
            line=re.sub("/","",line)
            wlcw+=line
        else:
            wlcw+line
    print('[*]In the rewriting...')
    wopen=open(path,'w')
    wopen.write(wlcw)
    wopen.close()
    foropen.close()
replace()