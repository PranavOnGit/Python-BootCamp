
class Fruite:
    def __init__(self, taste, color, size): 
        self.taste = taste
        self.color =  color
        self.size =  size

    def price_check(self):
        if self.size <= 6:
            return ' 34RS Per KG'
        else:
            return ' 30RS Per KG'

