fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    words=line.split()
    for elem in words: 
        if elem in lst: continue
    	lst.append(elem)
        lst.sort()
print(lst)
