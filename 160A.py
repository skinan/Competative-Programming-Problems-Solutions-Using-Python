# CodeForces
# 160A - Twins
# Strings and Greedy Algorithm based problem.


def main():
    num = int(input())
    temp_list = input().split(" ")
    coins = []
    # Make another list to convert all list elements to <int> type.
    for i in range(num):
        coins.append(int(temp_list[i]))
    coins.sort()
    coins_temp = []
    v = sum(coins)

    for i in reversed(range(0, num)):
        coins_temp.append(coins[i])
        x = sum(coins_temp)  # Summation of coins for me.
        y = v - x   # Summation of coins for my brother.
        if x > y:
            break
        del x, y

    print(len(coins_temp))


if __name__ == "__main__":
    main()
