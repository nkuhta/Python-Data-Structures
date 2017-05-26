##############################################################
#########        convert file to uppercase        ############
##############################################################

fname = input('Enter filename: ')

try:
    fhand = open(fname)
except:
    print('file does not exist')
    exit()

for line in fhand:
    print(line.upper())
