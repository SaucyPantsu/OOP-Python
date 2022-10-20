# Word Scrambling Code
# This code takes an input of words from the input terminal, and scrambles the letters
# Ryan McLoughlin C21431604

# breaking a string into a list
def convert_to_list(string):
    list_split = []
    list_split[:0] = string
    return list_split


# input a string
sentence_string = input("Please Put a Sentence here ->")

# lowercase the string
sentence_string = sentence_string.lower()
# split the string
split_string = sentence_string.split()
# index for reinserting elements
i = 0
for index in split_string:
    scrambled = index.split()
    if len(index) > 3:
        if len(index) > 4:
            # scrambling code
            for other_index in scrambled:
                length = len(other_index)  # find the length of the array
                divider = length//2  # ensure the middle element to move is a while number
                word = convert_to_list(other_index)  # make the single element into an array again
                # scramble some elements
                word[1], word[divider], word[length-3] = word[length-3], word[divider], word[1]
                scrambled = "".join(word)  # recombine the array into an element
            split_string.insert(i + 1, scrambled)  # adding elements back to an array
            del(split_string[i])  # deleting the original element the scrambling code replaced
            i = i + 1

        else:
            # scrambling code
            for other_index in scrambled:
                length = len(other_index)  # find the length of the array
                divider = length // 2  # ensure the middle element to move is a while number
                word = convert_to_list(other_index)  # make the single element into an array again
                word[1], word[divider], word[length - 2] = word[length - 2], word[divider], word[
                    1]  # scramble some elements
                scrambled = "".join(word)  # recombine the array into an element
            split_string.insert(i + 1, scrambled)  # adding elements back to an array
            del (split_string[i])  # deleting the original element the scrambling code replaced
            i = i + 1

    else:
        i = i + 1
# Combine the string back into a readable format and print
final_string = " ".join(split_string)
print(final_string)