#Comma removal program
#Ryan McLoughlin 29/9/22
#TU857/2

print("Strings Input")

name_string = 'Bianca,Louise,Clara,Phelan,Dublin,Ireland'#initialise string
new_string = name_string.replace(',',' ')#remove commas
print(new_string)#print string


#Concatenate strings program
#Ryan McLoughlin 29/9/22
#TU857/2

print('Concatenate program')

string_one = input('please input a string ->')#input string one
string_two = input('please input a second string ->')#input sting two
new_string = string_one + ' ' + string_two #combine strings
print(new_string)#print string unedited

print('The new_string is this long:', len(new_string))#output string length
print(new_string.upper())#print string in uppercase

if(new_string.count('Hello') >= 1):##if there is one hello or more
    print('Hello appears ',new_string.count('Hello'),' times')#print this message
else:
    print('-1')#else print -1




