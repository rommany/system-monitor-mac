import os
from rich import repr, print
import re
import subprocess

hostname = 'google.com'

cmd = f"ping -c 1 {hostname}"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]

print(output.decode())

response = output.decode()

# #response = os.system("ping -c 1 " + hostname)

regex = re.compile(r'.+bytes from (\S+)')

match = regex.match(str(response))

if match:
    pass
    print( f"{match}")

#print(response)
exit(0)
#and then check the response...
if response == 0:
  print (hostname), 'is up!'
else:
  print (hostname), 'is down!'
