# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:44:18 2024

@author: Linnea Good
"""

class Fish:
    def __init__(self):
        self.members = ["Tuna", "Salmon", "Koi"]
        
    def printMembers(self):
        print("Harmless fish:")
        for member in self.members:
            print("\t%s" % member)