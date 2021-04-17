# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fname="mbox-short.txt"
fh = open(fname)
count=0
avg=0
sm=0
for line in fh:
    ln=line.rstrip()
    if ln.startswith("X-DSPAM-Confidence:"):
        t=ln.find("0")
        v=float(ln[t:])
        count+=1
        sm=sm+v
 
avg=sm/count
print("Average spam confidence:" , avg)
