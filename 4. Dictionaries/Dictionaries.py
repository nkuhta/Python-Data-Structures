##############################################################
#################         Dictionary          ################
##############################################################

#   List is linear organized by index number

#   A dictionary has labels, there is no numerical order, just a label

#   Label = Key,  Keys and Values

purse=dict()

#   assign purse keys with values
purse['money']=12
purse['candy']=3
purse['tissues']=75
#   purse = {'money': 12, 'candy': 3, 'tissues': 75}..{'label': value,...,}

print("purse =",purse)
print("purse['candy'] =",purse['candy'])
purse['candy']=purse['candy']+2  #  add more candy :)
print("purse now =",purse)

##############################################################
#################         Assignment          ################
##############################################################

print('')
print('************   Assignment   ******************')

ddd = dict()
ddd['age']=21
ddd['course']=182
print("ddd =",ddd)
#   reassign age
ddd['age']=23
print("ddd after age reassign =",ddd)

#   English Key and spanish word value dictionary
eng2sp={'one':'uno','two':'dos','three':'tres'}
print("eng2sp =",eng2sp)
print('len(eng2sp) =',len(eng2sp))
#   Is 'one' a key?
print("'one' in eng2sp -->",'one' in eng2sp)
#   Is 'uno' a key?
print("'uno' in eng2sp -->",'uno' in eng2sp)

#   make a list of the dictionary Values with .values()
vals = list(eng2sp.values())
print("'uno' in vals --> ",'uno' in vals)

#   make a string into a dictionary
d=dict()
str='brontosaurus'
for i in str:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print("str_dic",d)

#  Equivalent .get() chararcter counting code
d=dict()
str='brontosaurus'
for i in str:
    d[i]=d.get(i,0)+1
print("str_dic",d)

##############################################################
################            Get             ##################
##############################################################
print('')
print('************   Get   ******************')
#   If you want to count how many times a name comes up etc.
#   you can use the get command to see if a name is in a list
#   then assign a default value (zero) when it's note

counts=dict()
#   List of names
names=['cs','cw','zq','cw']

for name in names:
    #   assign the name key to create or add one
    counts[name]=counts.get(name,0)+1
print(counts)

##############################################################
#############            Counting           ##################
##############################################################
print('')
print('************    Counting    ******************')

counts=dict()
line=input('enter a line of text\n')

#   split by spaces
words=line.split()
print('words =',words)

#   Make a word occurance dictionary, counts for each word
print('counting....')
for word in words:
    #   create and or update the word variable
    counts[word]=counts.get(word,0)+1
print('counts =',counts)

#####################################################################################
#############            Definite loops and Dictionaries           ##################
#####################################################################################
print('')
print('************    For loops and Dictionaries   ******************')

counts={'chuck':1,'fred':42,'jan':100}
print('counts =',counts)

for key in counts:
    print('key =',key,', counts[key] =',counts[key])

#####################################################################################
###########           Retrieving lists of keys and values            ################
#####################################################################################
print('')
print('************    Getting lists of keys and values    ******************')

jjj={'chuck':1,'fred':42,'jan':100}

#   list of keys
print(list(jjj))
print(jjj.keys())
#   list of values
print(jjj.values())
#   list of items
print(jjj.items())

#   Two Iteraction variables!!!

#   work your way through the tuple variables at the same time with two iteration variables
for aaa,bbb in jjj.items():
    print(aaa,bbb)

################################################################################
###########           Word Counts from first lecture            ################
################################################################################
print('')
print('************    Counting words    ******************')

name = input('enter filename: ')
handle=open(name,'r')
#   make one long string
text=handle.read()
#   split into a list of words
words=text.split()

counts=dict()
for word in words:
    #   create or add one
    counts[word]=counts.get(word,0)+1

bigcount=None
bigword=None
#   Find the largest count and corresponding word(key)
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count


print('bigword =',bigword,', bigcount =',bigcount)
