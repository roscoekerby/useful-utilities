import os

cmd = 'apt list --upgradeable > upgrades.txt'
os.system(cmd)

count = 0 
upgrade_list = []

with open("upgrades.txt", "r") as f:
  for line in f:
    stripped_line = line.strip()
    if count > 0:
    	try:
    		u = stripped_line.split("/")
    		u = u[0]
    		upgrade_list.append(u)    		
    	except:
    		x = 0
    count = count + 1
    
for u in upgrade_list:
	cmd = 'sudo apt-get install '  + u
	os.system(cmd)
