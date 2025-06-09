# word_count.py

# multi-line string using triple quotation marks

text = """
is is is is is this is a paragraph of text
that spans multiple line
there is a lot of text
with many different line breaks
"""

textx = """
one 
two two
three three three
"""

print (text)

words = text.split()
print (words)

# set will give a unique list of the words
word_list = set(words)
print (word_list)


# count how many of each word
word_count = {} # empty dictionary
#word_count = { 1, 2, 1, 2} # set
#word_count = {"one": 0} # dictionary with 1 key

for word in words:

    if word in word_count:
        # subsequent encountering this word
        word_count[word] = word_count[word] + 1
    else:
        # first time encountering this word
        word_count[word] = 1

print (word_count)