# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:44:18 2024

@author: Linnea Good
"""

class Fish:
    def __init__(self):
        self.members = ["Piranha", "Electric eel", "Shark?"]
        
    def printMembers(self):
        print("Dangerous fish:")
        for member in self.members:
            print("\t%s" % member)