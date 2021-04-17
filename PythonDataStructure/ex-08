name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=dict()
for line in handle:
    if not line.startswith("From"): continue
    line=line.rstrip()
    words=line.split()
    if len(words)>2:
        time=words[5]
        time=time.split(":")
        hour=time[0]
        lst[hour]=lst.get(hour,0)+1
        
Hours=list()
for k,v in lst.items():
    values=k,v
    Hours.append(values)
    
Hours=sorted(Hours)
for k,v in Hours:
	print(k,v)
