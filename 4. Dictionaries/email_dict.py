################################################################################
###########         Email Address Dictionary from file          ################
################################################################################

#  Make the email dict() out of the given filename
fname=input('input filename:')
fhand=open(fname)
email_dic=dict()

for line in fhand:
    if line.startswith('From:'):
        line=line.split()
        email=line[1]
        email_dic[email]=email_dic.get(email,0)+1
print('email dictionary =',email_dic)

#   find the maximum email counts
max_email_counts = 0
max_email_key = 0

for key in email_dic:
    if email_dic[key] > max_email_counts:
        max_email_counts = email_dic[key]
        max_email_key = key
print('\nmost frequent email address -  corresponding counts')
print(max_email_key,max_email_counts)
