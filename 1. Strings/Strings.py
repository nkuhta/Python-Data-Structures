##############################################################
#####################      Strings      ######################
##############################################################

#   A string is a sequence of chararcters
#   can either use "" or ''

str1 = 'hello'
str2 = ' there'

#  string conjugation (addition)
bob = str1 + str2

print(bob)

str3 = '123'
#   below won't work
#   str3 = str3 + 1

#   but using the int() command will work
x = int(str3)+1
print(x)

#  string inputs
name = input('Enter name: ')
print(name)

apple = input("Enter integer: ")
x=int(apple)-10
print("Int - 10 =",x)

##############################################################
############      Indexing Inside Strings      ###############
##############################################################
print("")
print("************   String Indexing    **********")

fruit = 'banana'
#  note python Indexing starts at ZERO
letter = fruit[1]   #  so this is the second letter
print(letter)

n=3
w = fruit[n-1]
print(w)

zot = 'abc'
#   index out of bounds - string index out of range
zot[2]

#   length function
print(len(zot))

##############################################################
#############      Looping Inside Strings      ###############
##############################################################
print("")
print("************   Looping in Strings    **********")

fruit = 'banana'
index = 0

#  indefinite loop
while index < len(fruit):
    letter = fruit[index]
    #  print out the array index and corresponding array string value
    print(index,letter)
    index = index + 1

print("")
#   definite Loop
fruit = "apple"
for letter in fruit:
    print(letter)

print("")
#  looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter=="a":
        count=count+1
print("Number of a's in",word,"=",count)   #  print number of a's in word

##############################################################
################      Slicing Strings      ###################
##############################################################
print("")
print("************   Slicing in Strings    **********")

s = 'Monty Python'

#   [start : up_to_but_not_including]

#  slice up and grab only some array elements
print(s[0:4])
print(s[6:7])
print(s[6:20])   #  traceback
print(len(s))

#  leaving off the first or last slice number results in beginning/end assumption

print(s[:2])
print(s[8:])
#  below command prints from beginning to end
print(s[:])

##############################################################
##################      In Operator      #####################
##############################################################
print("")
print("************   In Operator    **********")

fruit = 'banana'

print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'a' in fruit:
    print("a is in fruit name string")

##############################################################
#############      String Comparisons      ###################
##############################################################
print("")
print("************   String Comparisons    **********")

word='pear'

if word == 'banana':
    print('All right, bananas')

if word < 'banana':
    print("your word,",word,'comes before banana')
elif word > 'banana':
     print("your word,",word,'comes after banana')
else:
    print('all right, bananas')

##############################################################
###############      String Libraries      ###################
##############################################################
print("")
print("************   String Libraries    **********")

greet = 'Hello BOB'
#   .lower() makes everything lowercase
zap = greet.lower()
print(zap)

print("Hi There".lower())
print("Hi There".upper())

stuff = "Hello World"
#   print that stuff has a string type
print(type(stuff))
#   print the directory of Operations you can use on the stuff string
print(dir(stuff))

##############################################################
###############      Searching a String      #################
##############################################################
print("")
print("************   Searching/Replacing a String    **********")

fruit = 'banana'

#   pos = in which array position do you find the first instance of 'na'
pos=fruit.find('na')
print(pos)
#   aa = in which array element do you find 'z' in the fruit string (-1 = none)
aa = fruit.find('z')
print(aa)

#  search and replace
greet = "Hello Bob"

nstr = greet.replace("Bob",'Jane')
print(nstr)
nstr = greet.replace("o",'X')
print(nstr)

##############################################################
###############     Stripping Whitespace      ################
##############################################################
print("")
print("************   Stripping String Whitespace    **********")

greet = " Hello Bob   "
#   left strip
print(greet.lstrip())
#   right strip
print(greet.rstrip())
#   strip all Whitespace on left and right side
print(greet.strip())

##############################################################
#################        Prefixes          ###################
##############################################################
print("")
print("************   Prefixes    **********")

line = "Please have a nice day"
print(line.startswith('Please'))
print(line.startswith('p'))

#  Parsing Text 

data = 'From Joe.Cool@bob.loblaw.edu Sat Jan 5 09:14:19 2009'

#   @ symbol array position
atpos = data.find('@')
print(atpos)

#   find the space position array index after the atpos
sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)
