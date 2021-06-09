#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import enchant
d = enchant.Dict("en_US")
# print(d.check("Hello"))


with open("c:/Users/FENG/OneDrive/English/知米自定义词库/redbook/www.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)
    #english_words = set(word.strip() for word in word_file)

# def is_english_word(word):
#     return word.lower() in english_words
#
# print is_english_word("ham")


for word in english_words:
    if not d.check(word):
        print(word)
