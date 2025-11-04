import re

# File opening
with open("preproinsulin-seq.txt", "r") as f:
    data = f.read()

# 1. Text cleaning with regex
cleaned = re.sub(r'ORIGIN', '', data)        # Remove ORIGIN
cleaned = re.sub(r'//', '', cleaned)         # Remove //
cleaned = re.sub(r'\d+', '', cleaned)        # Remove numbers
cleaned = re.sub(r'\s+', '', cleaned)        # remove all spaces and line breaks


# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = cleaned
print(preproInsulin)
print("Total Characters:", len(preproInsulin))

# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = preproInsulin[0:24]  
bInsulin = preproInsulin[24:54]
cInsulin = preproInsulin[54:89]
aInsulin = preproInsulin[89:110]
insulin = bInsulin + aInsulin

pKR = {
        'y': 10.07,
        'c': 8.18,
        'k': 10.53,
        'h': 6.00,
        'r': 12.48,
        'd': 3.65,
        'e': 4.25,
       }

seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

print(seqCount)

pH = 0

while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))

    print('{0:.2f}'.format(pH), netCharge)
    pH +=1

# check the excel version too : insulin.xlsx
