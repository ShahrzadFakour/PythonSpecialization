import re
handle=open('regex_sum_1085766.txt')
sumOf= 0
for line in handle: 
    y= re.findall('[0-9]+', line)
    for item in y:
        value=int(item)
        sumOf= sumOf + value  

print(sumOf)
