##############################################################
################        Open Files          ##################
##############################################################

#   open(filename,mode)
#   mode = 'r', 'w' (read/write)
#   make the .txt file in same directory as the python code

data = open('mbox.txt','r')
print(data)

##############################################################
##################        New Line         ###################
##############################################################
print('')
print('************   New Line    ******************')

#   \n creates newline
stuff = 'hello\nworld!'
print(stuff)

stuff = "X\nY"
print(stuff)
#   show that the \n is one chararcter
print(len(stuff))

##############################################################
###########        File Handle sequence          #############
##############################################################
print('')
print('************    File Handle Sequence    ******************')

xfile=open('mbox-short.txt')

#   For each line (row) in xfile, print it out
#   for line in xfile:
#       print(line)

#   Counting lines in a File
fhand=open('mbox.txt','r')
count=0
for line in fhand:
    count=count+1
print('line count =',count)

##############################################################
############        Read the Whole File          #############
##############################################################
print('')
print('************    Read the Whole File    ******************')

fhand = open('mbox-short.txt')
#   read the whole file (note this is memory intensive)
inp = fhand.read()
#   print how many chararcters in the whole file
print(len(inp))
#   print the first 20 inp chararcters
print(inp[:20])

#####################################################################
############        Searching Through the File          #############
#####################################################################
print('')
print('************    Searching Through the File    ******************')

fhand = open('mbox-short.txt')

for line in fhand:
    if line.startswith('From:'):
        #   this gets rid of right Whitespace, and the implied \n
        line=line.rstrip()
        #   This adds it's own \n after every print() command
        print(line)

print('')

fhand = open('mbox-short.txt')
#   Skipping with continue
for line in fhand:
    line=line.rstrip()
    #  Skip uninteresting lines
    if not line.startswith('From:'):
        continue
    print(line)

print('')

#  Using in to select lines
fhand = open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

print('')

#  Prompt for filename
fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print("File does not exist")
    exit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were %d lines starting with Subject: in %s'%(count,fname))
