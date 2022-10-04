#Concatenate strings program
#Ryan McLoughlin 29/9/22
#TU857/2

print('Concatenate program')
string_one = input('please input a string ->')
string_two = input('please input a second string ->')
new_string = string_one + ' ' + string_two
print(new_string)

print('The new_string is this long:', len(new_string))
print(new_string.upper())

if(new_string.count('Hello') >= 1):
    print('Hello appears ',new_string.count('Hello'),' times')
else:
    print('-1')




