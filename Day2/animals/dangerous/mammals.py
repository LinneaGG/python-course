# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Mammals:
    def __init__(self):
        self.members = ["Tiger", "Bear", "Hippo"]
        
    def printMembers(self):
        print("Dangerous mammals:")
        for member in self.members:
            print("\t%s" % member)
            