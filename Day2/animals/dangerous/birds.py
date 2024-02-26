# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:46:54 2024

@author: Linnea Good
"""

class Birds:
    def __init__(self):
        self.members = ["Eagle", "Hawk", "Vulture"]
        
    def printMembers(self):
        print("Dangerous birds:")
        for member in self.members:
            print("\t%s" % member)