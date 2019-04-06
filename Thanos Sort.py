# CodeForces
# 1145A- Thanos Sort
# April Fool Day Contest 2019

#Thanos Sort is a sorting algorithm which removes half of the list/array until it is perfectly balanced.

def thanos_sort(y):

    for i in range(len(y) - 1):

        if int(y[i]) > int(y[i + 1]):  # If the list is not sorted in decreasing order.
            if i < int(len(y)/2):
                del y[:int(len(y)/2)]  # remove first "n" elements of the list
            else:
                del y[int(len(y) / 2):]  # remove last "n" elements of the list

            return thanos_sort(y)

    return len(y)


x = input()  # Get the size of the array.
y = input().split(" ")  # Get the string and split it to make list(array).

# Finally print the length of the array after thanos sorting.
print(thanos_sort(y))
