################################################################################
###########         Email Address Dictionary from file          ################
################################################################################

fname=input('input filename:')
fhand=open(fname)
email_dic=dict()

for line in fhand:
    if line.startswith('From:'):
        line=line.split()
        email=line[1]
        email_dic[email]=email_dic.get(email,0)+1
print('email dictionary =',email_dic)
