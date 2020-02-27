import random

random_array = [] #initialize empty array to hold random values
sort_func_array = [] # empty array to sort with built in method
number = 0 # holds each randomly generated value

for x in range(10):
  number = random.randint(1,101) #10 random values of numbers between 1 and 100
  random_array.append(number)
  sort_func_array.append(number)

# display original random array
######
print "Random Array"
for x in random_array:
    print x

lowest = 100
index = 0 ## index of lowest
x_index = 0
for x in random_array:
    y_index = 0
    for y in random_array:
        if(y_index < x_index):
            y_index += 1
            continue
        if(y < lowest):
            lowest = y
            index = y_index 
        y_index += 1
    random_array[index] = random_array[x_index]
    random_array[x_index] = lowest
    x_index += 1
    lowest = 100

# display sorted array
print "Sorted Array"
for x in random_array:
    print x