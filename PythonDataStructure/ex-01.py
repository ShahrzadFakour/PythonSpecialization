text = "X-DSPAM-Confidence:    0.8475";
twoPoint=text.find(":")
rest=text[twoPoint+1 :]
num=float(rest.lstrip())
print(num)
