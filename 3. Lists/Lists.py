##############################################################
################         Python Lists          ###############
##############################################################

#   Lists are variable Collections of assigned chararcters (string,number,chararcter)

#  Lists have [], and indexing begins at zero

friends = ['Joe','Glenn','Sally']
carryon = ['socks','shirt','perfume']

#   print everything up to but not including element 2 in the carryon
print('carryon[:2] =',carryon[:2])

#  Simple variables are not Collections
not_a_list = 10

#  numeric list
num_list = [1,12,24]

#  color string name list
col_list = ['red','yellow','bluE']

#  Lists can have multiple types
mult_list = ['red',24,98.6]
print('mult_list =',mult_list)
print('type(mult_list[2]) =',type(mult_list[2]))
print('mult_list[2] =',mult_list[2])

#  List within a list
layer_list = [1,[5,6],7]
print('layer_list =',layer_list)
#  print all of the 1st element
print('layer_list[1][:] =',layer_list[1][:])
#  print the 1st entry of the first element
print('layer_list[1][1] =',layer_list[1][1])

##############################################################
#############        Lists are Mutable          ##############
##############################################################
print('')
print('************   Mutable (reassign)    ******************')

#   You can reassign list values
org_list = [1,2,3,5,8,13,21]
org_list[2] = 44

print(org_list)

##############################################################
#############        Lists length len()          #############
##############################################################
print('')
print('************   len()    ******************')

greet = 'hello bob'
#   print the number of chararcters in greet, note space is a chararcter
print('greet =',greet)
print('len(greet) =',len(greet))

x = [1,3,'joe',99]
#   print the number of elements in the list x
print('x =',x)
print('len(x) =',len(x))

print('friends =',friends)
print('len(friends) =',len(friends))

##############################################################
###########        Range function, range()         ###########
##############################################################
print('')
print('************   range()    ******************')

#   range() creates lists, range(4) has elements up to but not including 4.
range_4 = list(range(4))
print('range(4) =',range_4)
print('length of range(4) =',len(range_4))

#print('i in range (4)')
#   print i in range(4)
for i in range(4):
    #print(i)
    continue

print('i in range (3,6)')
#   print i in range (3,6)
for i in range(3,6):
    print(i)

print('friends =',friends)
print('range(len(friends)) =',range(len(friends)))

##############################################################
############        for loops with Lists         #############
##############################################################
print('')
print('************   for loops with Lists    ******************')

#   print happy new year: person, where person is each element in the friends list
for person in friends:
    print("happy new year:",person)

#   Equivalent range() loop
for i in range(len(friends)):
    person=friends[i]
    print(person)

##############################################################
##############        Concatinate Lists         ##############
##############################################################
print('')
print('************   List Concatinate with +    ******************')

a = [1,2,3]
b = [4,5,6]
#   Concatinate or append lists together by adding
c = a + b

print(c)

##############################################################
################         Slicing Lists         ###############
##############################################################
print('')
print('************   Slicing Lists    ******************')

t = [9,41,12,3,74,15]
print('t =',t)
print('t[1:3] =',t[1:3])
print('t[:4] =',t[:4])
print('t[3:]',t[3:])

#   Remember [start : up_to_but_not_including] structure

##############################################################
################         List Methods         ################
##############################################################
print('')
print('************   List Methods     ******************')

#   empty list
x = list()
#   print list type
print(type(x))
#   print methods you can use with a list
print('List Methods: \n',dir(x))
print('')

#   build up the x list using append command
x.append('book')
x.append('99')
print(x)
x.append('cookie')
print(x)

#   is something in a list
some = [1,9,21,10,16]
print('some =',some)
print('is 9 in some?',9 in some)
print('is 15 in some?',15 in some)
print('is 20 not in some?',20 not in some)

#   These logical statements do not modify the list

print('some :',some)
#   overwrites some with the numerically ordered list
some.sort()
print('some.sort() =',some)

print('friends :',friends)
#   overwrites friends with the alphabetically ordered list
friends.sort()
print('friends.sort() =',friends)

##############################################################
##############         List Functions         ################
##############################################################
print('')
print('************   List Functions     ******************')

nums = [3,41,12,9,74,15]

print('nums =',nums)
print('len(nums) =',len(nums))
print('max(nums) =',max(nums))
print('min(nums) =',min(nums))
print('sum(nums) =',sum(nums))
print('average(nums) =',sum(nums)/len(nums))

#   Averaging with a list
total = 0
count = 0

#  Averaging a list
while True:
    inp = input('Enter a number:')
    if inp == 'done':
        break
    else:
        try:
            value = float(inp)
            total = total + value
            count = count +1
        except:
            print('not a number, try again')

average = total/count
print('input average =',average)

#  another way to append input values to the list
numlist=list()
#  Note you need to think about memory if this list becomes large
while True:
    inp = input('Enter a number:')
    if inp=='done':break
    try:
        value=float(inp)
        numlist.append(value)
    except:
        print('not a number, please try again')
average=sum(numlist)/len(numlist)
print('Average of numlist =',average)

##############################################################
##############         Strings and Lists         #############
##############################################################
print('')
print('************   Strings and Lists     ******************')

abc = 'with three words'
#   split command turn string into list of strings, splitting where the spaces are
stuff = abc.split()

print('abc =',abc)
print('abc.split() =',stuff)
print('len(stuff) =',len(stuff))
print('stuff[0] =',stuff[0])

for w in stuff:
    print(w)


line = 'first;second;third'
#   Now split on the semi-colon
s_line = line.split(';')
print('split line =',s_line[:])


#  Parsing some mailbox data

fhand = open('mbox-short.txt')
for line in fhand:
    #   Strip off the lines right chararcters (ie. spaces and \n)
    line = line.rstrip()
    #   If a line in the file handle doesn't start with 'From ' go to the next one.
    if not line.startswith('From '):continue
    #   split the line that starts with 'From ' into a list of chararcters
    words = line.split()

print('line.split() =',words)
print('day =',words[2])

##############################################################
################         Double Split         ################
##############################################################
print('')
print('************     Double Split      ******************')
#   The first split happened above splitting the line by spaces
email=words[1]
#   Now split the email address by the @ sign
pieces=email.split('@')
#   print the email address before and after the @ symbol
print(pieces)
print('email domain =',pieces[1])
