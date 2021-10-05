import json
import os

f = open ('requires.json', "r")
api=json.loads(f.read())
check=os.popen('py -m pip list').read()
needed=[]
print("Check pips...")
for i in api['list']:
    if i not in check:
        needed.append(i)
    else:
        print(i,"already installed")

for i in needed:
    os.system("py -m pip install {}".format(i))
