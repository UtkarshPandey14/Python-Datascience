# flexible parameter in a function
# *args, **kwargs

def mean(*numbers):
    total = 0
    for item in numbers:
        if isinstance(item,(int,float)):
            total += item
    return total / len(numbers)

def report(**marks):
    total_marks = 0
    for k,v in marks.items():
        print(f'{k} got {v} marks')
        total_marks += v
    return total_marks

print(report(ram=80,shyam=90,hari=85,shy=56))
print(mean(1,2,3,1))
print(mean(1,2,3,4,5,6,7,8,9,10))
print(mean(12,34,55,32,12,345,12,67,89,987,546,34))
print(mean(12,'a',34,'123',45,67,98))