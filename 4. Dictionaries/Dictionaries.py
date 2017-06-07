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

##############################################################
################            Get             ##################
##############################################################
