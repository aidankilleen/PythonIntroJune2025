# tuple_uses.py

# use #1 = return multiple values from a function
def process_list(numbers):

    print (numbers)
    s = sum(numbers)

    avg = s / len(numbers)
    return (s, avg)

l = [10, 6, 4, 8, 2, 9, 3, 1]

result = process_list(l)
print (result)

# result[0] = 12345566

print (f"The total is {result[0]}, the average is {result[1]}")


# use #2 - upacking

t = (1, 2, 3)

#one = t[0]
#two = t[1]
#three = t[2]

# unpack the items from the tuple using tuple assignments
(one, two, three) = t

print (one, two, three)


# use #3 - swap two variable

a = 10
b = 20
print (a, b)

#swap
t = a
a = b
b = t

print (a, b)

# or us python tuples to swap without needing a temporary variable
# if a tuple is immutable how are a and b changing?
(a, b) = (b, a)
print (a, b)

# tuple uses #4
# if python knows something can't change - it can make the code more efficient



lst = [1,2,3,4]

t = tuple(lst)
print (lst)
print (t)

list_from_tuple = list(t)

print (list_from_tuple)


# NB
# python won't complain if you create a variable with the same name as something else
# in this case list was a built-in function but now it is a list
list = [1, 2, 3]

# now this code fails to run
#list_from_tuple = list(t)

#NB don't use built-in function names for your variables.

