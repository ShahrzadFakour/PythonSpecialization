name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
Dic=dict()
for line in handle:
    if not line.startswith('From'): continue
    if len(line)>2:
        words=line.split()
        emails=words[1]
        if len(words)>2:
			Dic[emails]=Dic.get(emails,0)+1
Hrepeat= None
Trepeat=None
for email,repeat in Dic.items():
    if Hrepeat is None or repeat > Trepeat:
        Hrepeat= email
        Trepeat=repeat
print(Hrepeat,Trepeat)
        
