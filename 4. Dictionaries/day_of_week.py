################################################################################
#################         Add up days of week for email         ################
################################################################################

#   filename
name = input('input filename: ')
handle = open(name,'r')

#   day of week dictionary
dow=dict()

for line in handle:
    if line.startswith('From'):
        mod=line.split()
        try:
            #   assign day of week key string
            day_of_week=mod[2]
            dow[day_of_week]=dow.get(day_of_week,0)+1
        except:
            continue
print(dow)
