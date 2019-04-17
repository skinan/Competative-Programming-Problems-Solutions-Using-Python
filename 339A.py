# Codeforces
# 339A - Helpful Maths

def main():
    # Get the input list.
    temp_list = input().split("+")

    main_list = []
    # Make another list to convert all list elements to <int> type.
    for i in range(len(temp_list)):
        main_list.append(int(temp_list[i]))
    # Sort the list.
    main_list.sort()
    
    # Again make another list to convert all list elements to <str> type.
    final_list = []
    for i in range(len(main_list)):
        final_list.append(str(main_list[i]))
    # Convert list to string and print it.
    print("+".join(final_list))


if __name__ == "__main__":
    main()
