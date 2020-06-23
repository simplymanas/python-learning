# Wordwrap
# using simple minimum algorithm
# from wikipedia:
# minimum length greedy algorithm
# other algorithm
# knuth
# Plass Tex
# (possible only if language provide this)
# What is word wrap
# continuing on a new line when a line is full, so each line fits into a screen length
# no horizontal scrolling
# benefit
# saves you from a new line charactr
# its a soft wrap unlike the hard wrap to create a new pargrpah
# soft return (shift + enter)
# Rules
# soft return at the end of the line after the end of a complete word
# or a puntuation followed by a complete word
# following a hyphen inside  a word
# Question
# Do you think word wrapping is an oprimisation problem

# Algorithm: minimum numbers of line
# greedy algorithm, put as many words as you can in one line as possible, and then move on to the next line
# do the same until  no more word are left

# SpaceLeft := LineWidth
# for each Word in Text
#     if (Width(Word) + SpaceWidth) > SpaceLeft
#         insert line break before Word in Text
#         SpaceLeft := LineWidth - Width(Word)
#     else
#         SpaceLeft := SpaceLeft - (Width(Word) + SpaceWidth)


# with dynamic programming , choose the position at which to break the line
# instead of choosing breaks greedily O(n2), n is the number of words in the line
# Tex typesetting system by Donald Knuth in 1977 had a greedy algorithm for line breaking algorithm
# another liner time alogirhtm was based on SMAWK alogrithm

# wisdom from internet
# the Knuth-Plass algorithm is also used in Adobe InDesign.
# http://www.eprg.org/G53DOC/pdfs/knuth-plass-breaking.pdf


import textwrap
# -*- coding: utf-8 -*-
# PEP 263 -- Defining Python Source Code Encodings

# https://github.com/python/cpython/blob/3.8/Lib/textwrap.py

# help(textwrap.fill)

text_to_wrap = '''\
"About CODA by Sanjay Vyas, [10-Apr-2020 at 1:15:19 AM]:
Incidentally.. CODA (CODeAlone) is also an English word.. which means "tail" or end of "concluding" part of a ballet or novel
My favourite music group - Led Zeppelin released last album of assorted tracks called CODA

Does anyone know what is equivalent of "CODA" in Indian Classical Music, where the musicians play at really high speed, before concluding? 😊'''

text_to_wrap = "This function wraps the input paragraph such that each line in the paragraph is at most width characters long. The wrap method returns a list of output lines. The returned list is empty if the wrapped output has no content."


# wrap the word and provide a list of lines
# print(textwrap.wrap(text_to_wrap, width=15))

# show the new paragraph
# print(textwrap.fill(text_to_wrap, width=5))


# Collapse and truncate the given text to fit in the given width.
# print(textwrap.shorten(text_to_wrap, width=55))

# chalo bhai log CODA khatam
#
# def wrapit(string, max_width):
#     s = ''
#     for i in range(0, len(string), max_width):
#         s += string[i:i + max_width]
#         s += '\n'
#     return s
#
#
# def wrapme(string, max_width):
#     return "\n".join([string[i:i + max_width] for i in range(0, len(string), max_width)])


def wrap(input_text, screen_length):
    left_spaces = screen_length
    spacewidth = 1  # setting 1 to default
    line=''

    words_from_input_text = input_text.split(' ')

    for word in words_from_input_text:
        if (len(word) + spacewidth) > left_spaces:
            # print('\n' + word + ' ')
            left_spaces = screen_length - len(word)
            line = line + '\n'
        else:
            # print(word + '*')
            line = line + ' ' + word

            left_spaces -= len(word) + spacewidth
    return line


def wordwrap(text, length):
    if not isinstance(text, str):
        raise ValueError('Not a string!')
    elif length <= 0:
        raise ValueError('Negative Value!')

    return "\n".join([_linewrap(line, length) for line in text.split("\n")])


def _linewrap(text, length):
    words = text.split() # split line into words
    temp = ""
    result = []

    for word in words:
        if temp=="" or len(temp + " " + word) <= length:
            temp += " " + word; # add word to line
        else:
            result.append(temp.strip())
            temp = word  # start new line

    if len(temp) != 0:
        result.append(temp.strip())

    return "\n".join(result)



# print(wrap(input_text=text_to_wrap, screen_length=50))
print(wordwrap(text=text_to_wrap, length=48))
