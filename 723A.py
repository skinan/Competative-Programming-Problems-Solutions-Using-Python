# CodeForces
# 723A - The New Year: Meeting Friends
# Math , Sorting, Implementation based problem.


def main():
    temp_list = input().split(" ")

    main_list = []
    # Make another list to convert all list elements to <int> type.
    for i in range(3):
        main_list.append(int(temp_list[i]))
    main_list.sort()  # Sort it.
    # Do the require mathematical calculation below.
    a = main_list[1] - main_list[0]  # Distance from middle one to first one.
    b = main_list[2] - main_list[1]  # Distance from middle one to last one.
    result = a + b
    print(result)


if __name__ == "__main__":
    main()
