import math

class Matematical:
    def squared(self, num):
        return num * num

   

class Pitagoras:
    def __init__(self, matematical):
        self.matematical = matematical
    def run(self, a, b):
        a_squared = self.matematical.squared(a)
        b_squared = self.matematical.squared(b)
        a_plus_b = a_squared + b_squared
        result = math.sqrt(a_plus_b)

        return result