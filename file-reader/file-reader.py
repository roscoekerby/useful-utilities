filename = 'file.txt' #  change file name here

with open(filename, "r") as f:
  for line in f:
  	line_removed_formatting = str(line).replace('\n','')
  	print(line_removed_formatting)
