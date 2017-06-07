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

##############################################################
################            Get             ##################
##############################################################

#   If you want to count how many times a name comes up etc.
#   you can use the get command to see if a name is in a list
#   then assign a default value (zero) when it's note
