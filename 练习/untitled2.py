# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:50:13 2016

@author: aa
"""

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
