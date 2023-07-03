#Sokheng Ka 1968133

import csv

input = input()

with open(input, 'r') as list_file:
    words_list = csv.reader(list_file)
    for row in words_list:
        list_of_words = row

no_dups = list(dict.fromkeys(list_of_words))
length = len(no_dups)

for i in range(length):
    print(no_dups[i], list_of_words.count(no_dups[i]))
