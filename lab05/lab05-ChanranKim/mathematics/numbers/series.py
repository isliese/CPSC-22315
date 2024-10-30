# Create a function named `sum` which receives a keyword parameter `list` 
# and returns the sum of all the values in the list.
def sum(*, list):
    sum = 0
    for i in list:
        sum += i
    return sum

# Create a function named `average` which receives a keyword parameter `list` 
# and returns the average of all the values in the list.
def average(*, list):
    sum = 0
    for i in list:
        sum += i
    average = sum / len(list)
    return average
    
