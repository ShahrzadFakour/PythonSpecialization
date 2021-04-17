# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    if fname=="words.txt":
		fh = open(fname)
except:
    print("file is not correct")
    quit()

for line in fh:
    fline=line.rstrip()
    fUpper=fline.upper()
    print(fUpper)
