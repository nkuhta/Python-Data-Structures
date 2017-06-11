##############################################################
###############            Tuples           ##################
##############################################################

#   Tuples are like lists, but () instead of []

#   Tuple
x = ('Glenn','Sally','Joe')

print("x[2] =",x[2])

y = (1,9,2)

print('max y =',max(y))

for iter in y:
    print(iter)

#   Tuples are Immutable, CANNOT alter the contents (like a string)

z = (5,4,3)
#   Trying the assignment below will cause traceback
#z[2]=0
#   Cannot sort/append/reverse
#   More Trackbacks
# z.sort()
# z.append(1)
# z.reverse()

l=list()
print(dir(l))
t=tuple()
print()
print(dir(t))

#   Why use Tuples?
#   More Efficient!!!

#   Use tuples when we create temporary lists that don't need to change

##############################################################
###############          Assignment           ################
##############################################################

print('')
print('********************   Assignment    *******************')

#   Make Assignment to a tuple
(x,y) = (4,'fred')
print(y)
#   Actually you don't need the first
a,b=(99,98)
print(a)

d = dict()
d['csev']=2
d['cwen']=4
#   dictionaries are 2 item tuples
for (k,v) in d.items():
    print(k,v)
tups=d.items()
print(tups)

##############################################################
##############          Comparisons           ################
##############################################################

print('')
print('********************   Comparisons    *******************')

#   Less than becomes true/false if the first instance is true/false
#   True 0 < 5
print((0,1,2) < (5,1,2))
#   True 1 < 3
print((0,1,200000) < (0,3,4))
#   False Sally < Fred
print(('Jones','Sally') < ('Jones','Fred'))
#   True Sally < Sam
print(('Jones','Sally') < ('Jones','Sam'))
#   True Jones > Adams
print(('Jones','Sally') > ('Adams','Sam'))

##############################################################
################          Sorting           ##################
##############################################################

print('')
print('********************   Sorting Lists of Tuples    *******************')


d = {'a':10,'c':22,'b':1}
#   Make a list if tuple dictionary items
t=list(d.items())
print(t)
#   sort by first tuple entry (key)
t.sort()
print('key sorted tuple list =',t)

#   Sort by values instead of keys
d = {'a':10,'c':22,'b':1}
tmp=list()
for k, v in d.items():
    #   reverse the tuple order when assigning to new list
    tmp.append((v,k))
print("tmp =",tmp)

tmp.sort()
print('value sorted tuple list =',tmp)
tmp.sort(reverse=True)
print('reverse value sorted tuple list =',tmp)

###########################################################################
################          10 most common words           ##################
###########################################################################

print('')
print('********************   10 most common words    *******************')

fhand=open('romeo.txt')
counts=dict()

for line in fhand:
    #   line word list
    words=line.split()
    for word in words:
        #   create counts dictionary
        counts[word]=counts.get(word,0)+1

lst=list()
for key,val in counts.items():
    #   create list with value first
    lst.append((val,key))

#   Sort by value
lst.sort(reverse=True)

for val,key in lst[:10]:
    print(key,val)

#   Shortened version (more advanced)
c={'a':10,'b':1,'c':22}
#   Sort by value in one line, by creating a sorted list of (value,key) tuples
print(sorted([ (v,k) for k,v in c.items() ]))
