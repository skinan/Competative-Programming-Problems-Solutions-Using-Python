# A. Diverse Strings
# CODEFORCES PROBLEM - 1144A


def diverse_string(x):
    x = str(x)
    lx = len(x)

    if lx == 1:
        return "Yes"

    y = sorted(x)  # Returns a sorted list to "y" in alphabetical order.

    y = list(dict.fromkeys(y))  # Ar first dict() converts the <list> type "y" to dictionary type and the list() convert
    # And the list() convert it to again to the <list> type class.(It is done to remove the repeated alphabets)

    # "y" is the identical and sorted alphabets list.
    # "x" is the main string.

    n = len(y) - 1

    # k = Get difference of ASCII value's of the first and last alphabet of the sorted and identical alphabets list.
    k = (int(ord(y[n])) - int(ord(y[0]))) + 1

    if lx != len(y):
        return "No"
    if lx == len(y) == k:
        return "Yes"
    else:
        return "No"


def main():
    number = int(input())  # number = How many strings to check.

    d = []

    for i in range(0, number):

        check_string = input()
        d.append(check_string)
        del check_string

    ans = ""
    for i in range(number):

        ans = ans + "\n" + str(diverse_string(d[i]))

    print(ans)


if __name__ == "__main__":
    main()
