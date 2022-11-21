# course: Object-oriented programming, year 2, semester 1
# academic year: 2022-23
# author: B. Schoen-Phelan
# date: Nov 2022
# purpose: Lab 6 Exceptions and Files

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html(self.my_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')
        index = 0
        # your code goes here!
        for index in the_dict:
            fo.write('<span style="font-size:' 'px"> HELLO </span>')

        fo.write('<span style="font-size: 20px"> HELLO </span>')

        fo.write('</div>\
            </body>\
            </html>')

        fo.close()


    # opens the input file gettisburg.txt
    # remember to open in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {}
        # your code goes here:

        return my_dict

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self, word, the_dict):
        # your code goes here

        return the_dict
# creates an instance of the WordCloud object
# remember first step after creation of an instance
# is that Python goes into the __init__ function


def convert_to_list(string):
    list_split = []
    list_split[:0] = string
    return list_split


index = 0
i = 0
dict_list = {}
wc = WordCloud()
biglist = open('gettisburg.txt', 'r')
biggest_list = list
for line in biglist:
    word = line.lower().split()
    for index in range(len(word)):
        if word[index] not in dict_list:
            instance = word.count(word[index])
            element = {word[index]: instance}
            dict_list.update(element)

print(dict_list)

wc.create_html(dict_list)






