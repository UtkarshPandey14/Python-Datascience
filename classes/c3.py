import random

class Mylist(list):   # inherits from list
    def shuffle(self):
        random.shuffle(self)


    def get_random(self):
        return random.choice(self)

# object

a = Mylist([12,123,23,23,45,67,87,98,66,43,567,88])
a.sort()
print(a)
a.shuffle()
print(a)
print("random item from list = ",a.get_random())
