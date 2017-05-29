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
