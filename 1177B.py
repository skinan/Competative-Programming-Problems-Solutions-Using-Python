# Codeforces
# 1177B - Digit Sequences (Hard Edition)
# I have used Permutation-Combination basic knowledge to solve this.
# Start of Code:

k = int(input())
# If k is less than 9 then print k, it is the answer.
if k <= 9:
    print(k)

# Otherwise follow the procedure below.
else:
    length = len(str(k))  # Number of digits in k is calculated as length firstly.
    places_occupied = 0  # Places occupied by required numbers are 0 at the beginning.
    
    # Start a loop below to calculate how many places can be occupied by whole numbers.
    for i in range(length - 1):
        places_occupied += (9*(10**i))*(i + 1)
        temp = places_occupied + (9*(10**(i + 1)))*(i + 2)  # Predict the result of next iteration.
        if temp > k:
            length = i + 2  # Change the value of length.
            break

    digits_string = ""  # A string variable to produce a number of nth "1" digits. Example: 111,1111 etc
    for i in range(length - 1):
        digits_string = digits_string + "1"

    # Numbers which are already used to occupy the certain number of places got previously.
    numbers_passed = 9 * int(digits_string)
    places_left = k - places_occupied

    # Final calculation part to determine what is the last number required to satisfy "k" number of places in a string.
    if places_left % length == 0:
        numbers_required = places_left // length
        answer_string = str(numbers_passed + numbers_required)
        print(answer_string[len(answer_string) - 1])  # In this case, last character of string is the answer.
    else:
        numbers_required = (places_left // length) + 1
        answer_string = str(numbers_passed + numbers_required)
        find_index = (numbers_required * length) - places_left  # Here we need to find the index number to get result.
        print(answer_string[len(answer_string) - find_index - 1])
