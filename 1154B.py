# Codeforces
# 1154B - Make Them Equal

def equal(num):
    if len(num) == 0 or len(num) == 1:
        return 0
    elif len(num) == 2:
        value = (int(num[1]) - int(num[0]))
        if value % 2 == 0:
            value = int(value/2)
        return value
    elif len(num) == 3 and (int(num[2]) - int(num[1])) == (int(num[1]) - int(num[0])):
        return int(num[2] - num[1])
    else:
        return -1


def main():
    l = input()

    temp_list = input().split(" ")
    
    # Convert it to "dictonary" to remove duplicates from lists.
    temp_list = list(dict.fromkeys(temp_list))

    num = []
    # Make all the strings in temp_list <int> type data and append it to new list "num".
    for i in range(len(temp_list)):
       num.append(int(temp_list[i]))
    # Sort the list.
    num.sort()
    
    result = equal(num)
    print(result)


if __name__ == "__main__":
    main()
