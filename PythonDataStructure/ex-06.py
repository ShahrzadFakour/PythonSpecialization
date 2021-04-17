fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst=list()
email=list()
for line in fh:
    line=line.rstrip()
    if not line.startswith('From'): continue
    words=line.split()
    if len(words)>2:
        email=words[1]
        lst.append(email)
        print(email)
count=len(lst)	
print("There were", count, "lines in the file with From as the first word")
