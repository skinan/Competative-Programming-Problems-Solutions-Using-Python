# CodeForces
# 1005B - Delete from the Left


def main():
    s1 = input()  # First String.
    s2 = input()  # Second String.

    i = len(s1) - 1
    j = len(s2) - 1

    while i >= 0 and j >= 0:
        if s1[i] == s2[j]:  # Check whether the ith an jth elements of the following strings matches or not.
            i -= 1
            j -= 1
        else:               # break the loop whenever the match is not found.
            break

    result = (i + 1) + (j + 1)
    print(result)


if __name__ == "__main__":
    main()
