####################################################################
#################         Split out emails         #################
####################################################################

count=0
email_list=list()
#   file to split out emails from
fname = input('enter filename: ')
fhand = open(fname)

#   for each line in the file
for line in fhand:
    if line.startswith("From"):
        #   split out the from lines
        mail_str=line.split()
        #   the [1] element is the email address, append uniques to email_list
        while mail_str[1] not in email_list:
            email_list.append(mail_str[1])
            #   count the unique email addresses
            count=count+1

for i in range(len(email_list)):
    print(email_list[i])
print('there were %d unique email addresses'%count)
