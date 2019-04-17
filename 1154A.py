# Codeforces
# 1154A - Restoring Three Numbers.

def main():
    temp = input().split(" ")  # Get the inputs in a temporary list.
    
    num = []
    
    # Convert all the list elements to integer type, and append it to a new list.
    for i in range(len(temp)):
        num.append(int(temp[i]))
    
    # Sort the list.
    num = sorted(num)
    
    # Mathematical operations are done below to find the three numbers.     
    a = int(num[3]) - int(num[0])

    b = int(num[3]) - int(num[1])

    c = int(num[3]) - int(num[2])

    print(a, b, c)


if __name__ == "__main__":
    main()
    
