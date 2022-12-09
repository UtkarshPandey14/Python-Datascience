f = lambda x : x * 5                                           # a lambda function
print(f(3),f(2124),f(-2134))

# actual usage of lambda function
x = [23,45,66,22,87,42,82]

x2 = list(map(lambda i : i**2,x))     # map function
print(x2) 

a = [1,2,32,43,23,12,56,78,98]
b = [43,67,8,9,90,34,21,1,22]

ab = list(map(lambda i,j: i*j, a,b)) # map function with multiple list
print(ab)

#filter
evens = list(filter(lambda i:i %2 == 0,x))
print(evens)