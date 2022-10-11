# Sentence Manipulation
# C21431604 Ryan McLoughlin
# 6/10/22

# QA
sentence_list = list(input("Please Put a Sentence here ->")) # input a list
print(sentence_list) # print a list

# QB
sentence_string = input("Please Put a Sentence here ->") # input a string
print(sentence_string) #print string
split_string = sentence_string.split() #split the string

# QC
print(split_string) # print the split string
# QD
split_string.append(input("Please add to this sentence here ->")) # adding tp the split string

print(split_string) # printing split string
# QE
target_element = input("Which element do you want to remove? ") # making target string to remove
split_string.remove(target_element) # removing target string

# QF
print(split_string) # print string
print("There are ", split_string.count("cake"), "instances of cake in this string") # looking for cake in string
# QG
print(split_string[::-1]) # printing inverted string
# QH
print(split_string*3) # printing string *3
# QI
split_string[0], split_string[-1] = split_string[-1] , split_string[0] # switching element 0 with last element
print(split_string)
# QJ
print(len(split_string)) # printing length of string
