# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 13:22:07 2016

@author: aa
"""

class Person(object):
    def __init__(self,name,gender,age,**kw):
        self.name=name
        self.gender=gender
        self.age=age
        a=kw.keys()
        for i in a:
            setattr(self,a[0],kw[a[0]])

bob=Person('bob','male',18, job='student')