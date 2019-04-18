# Codeforces
# 1043A - Election

def main():
    num = int(input())
    # Get the input list.
    temp_list = input().split(" ")

    main_list = []
    # Make another list to convert all list elements to <int> type.
    for i in range(num):
        main_list.append(int(temp_list[i]))

    add = sum(main_list)  # add = Summation of all the list elements.
    k = max(main_list)   # k = Get the max integer from the following list.
    test_list = []
    z = 0  # z is used here to check for the correct result and iteration of loop.
    while add >= z:
        for i in range(len(main_list)):
            test_list[:] = [(k - j) for j in main_list]  # Subtract the value of "k" from all the elements of main_list.
            z = sum(test_list) 
        k += 1

    print(k - 1)


if __name__ == "__main__":
    main()
