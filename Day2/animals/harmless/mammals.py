# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Mammals:
    def __init__(self):
        self.members = ["Cat", "Capybara", "Mouse"]
        
    def printMembers(self):
        print("Harmless mammals:")
        for member in self.members:
            print("\t%s" % member)
            