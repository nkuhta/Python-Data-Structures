##############################################################
#########        compute the average spam         ############
##############################################################


#   X-DSPAM-Confidence:0.8475

#   Prompt for user input filename then search for the number and average

fname=input('Enter filename: ')

try:
    fhand = open(fname)
except:
    print("file does not exist")
    exit()

#  line iteration variable
count=0
#   spam value iteration variable that will be summed over
num=0

#  extract the spam confidence values and average them
for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        ival = line.find(":")
        numline = float(line[ival+1:].lstrip())
        count = count+1
        num = num + numline

avg = num/count

print('count = ',count)
print('average spam confidence = ',avg)
