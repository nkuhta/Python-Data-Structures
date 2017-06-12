###################################################################
###############            Time of Day           ##################
###################################################################

fhand=open('mbox-short.txt')
hour=dict()

for line in fhand:
    if line.startswith('From'):
        email=line.split()
        #   Only go for the longer lists with time elements
        if len(email) > 3:
            time=email[5]
            time=time.split(":")
            hour[time[0]]=hour.get(time[0],0)+1

#print(hour)

#   Sort the hours by occurance
t=list()
for (k,v) in hour.items():
    t.append((v,k))

t.sort(reverse=True)

print('Hour #emails')
for val,key in t:
    print(key,val)
