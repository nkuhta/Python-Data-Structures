##############################################################
#################         Word List          #################
##############################################################

#   We will populate this list with all words in given file
word_list=list()
#   Enter file name we want the word list of
fname = input('filename? ')
#   file handle
fhand=open(fname)

#  for each line in the file
for line in fhand:
    #   create a split list of words for each line.
    lsp = line.split()
    #   loop over each word in the list in the current line
    for i in range(len(lsp)):
        #   While the word in the split line word list is not in the global word list
        while lsp[i] not in word_list:
            #   append each word not in word_list to the list
            word_list.append(lsp[i])

#   Sort the word list
word_list.sort()
print(word_list)
