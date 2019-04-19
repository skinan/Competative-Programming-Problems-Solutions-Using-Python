# CodeForces
# 141A - Amusing Joke


def main():
    s1 = input()  # First String.
    s2 = input()  # Second String.
    s3 = input()  # Third String.
    z = []
    for i in s1:
        z.append(ord(i))  # Make a list with ASCII code of each character of string.
    for i in s2:
        z.append(ord(i))  # Append to that list with ASCII code of each character of string.
    z.sort()
    check = []
    for i in s3:
        check.append(ord(i))
    check.sort()
    if z == check:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
