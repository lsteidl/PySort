import random

total = 10 # number of array elements
random_array = [] #initialize empty array to hold random values
sort_func_array = [] # empty array to sort with built in method
number = 0 # holds each randomly generated value

for x in range(10):
  number = random.randint(1,100) #10 random values of numbers between 1 and 100
  random_array.append(number)
  sort_func_array.append(number)

# display original random array
######
print "Random Array"
for x in random_array:
    print x,

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
    lowest = 1000

print #spacing
#display built-in sorting of array
print "Built-in Sort Function"
sort_func_array.sort()
for x in sort_func_array:
    print x,

# display manual sorted array
print #spacing
print "Manual Sorted Array"
for x in random_array:
    print x,

#calculate average (mean)
sum = 0
for x in random_array:
    sum += x
average = sum / total
#display Mean
print #spacing
print "Mean: ", 
print average

#median
# if total is even, median = ( element # (total/2) + element # (total/2)-1 ) / 2 
# if total is odd.. 1 2 3 4 5 6 7 8 9, median is (total + 1) / 2
if(total % 2 == 0):
    median = ( random_array[(total/2)] + random_array[(total/2)-1] ) / 2
else:
    median = random_array[((total + 1) / 2)]
#display Median
print "Median: ", 
print median

#calculate Range
range = random_array[total - 1] - random_array[0]
#display Range
print "Range: ", 
print range