# CodeForces
# 432A - Choosing Teams


def main():
    num_list = input().split(" ")
    temp_list = input().split(" ")
    k = int(num_list[1])
    n = int(num_list[0])
    del num_list
    main_list = []
    # Make another list to convert all list elements to <int> type.
    for i in range(n):
        main_list.append(int(temp_list[i]))
    main_list.sort()  # Sort it.
    del temp_list

    main_list[:] = [(i + k) for i in main_list]
    final_list = []
    for i in range(int(n)):
        if main_list[i] <= 5:
            final_list.append(main_list[i])
    del main_list
    result = len(final_list)//3
    print(result)
    del final_list


if __name__ == "__main__":
    main()
