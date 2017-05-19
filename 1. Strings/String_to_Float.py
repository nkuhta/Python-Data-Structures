
##############################################################
########        Find then String to Float          ###########
##############################################################

#   Use find to return the str number after the colon below
#   Then convert is to a Float

str = 'x-dspam-confidence:  0.8475'

#  find the colon array value
colon_val = str.find(':')
#  double check
print(str[colon_val])

#  The number is everything starting from the entry after the colon, stripped of Whitespace
number = float(str[colon_val+1:].lstrip())
print(number)
print(type(number))
