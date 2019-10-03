# Codeforces
# Codeforces Round #590 (Div. 3)
# A. Equalize Prices Again
# Problem Statement Link: https://codeforces.com/contest/1234/problem/A


def query(given_list):
    s = sum(given_list) // len(given_list)
    if sum(given_list) % len(given_list) == 0:
        return s
    else:
        return s + 1


def main():
    ans = []
    for i in range(int(input())):

        num = input()
        given_list = list(map(int,input().split(" ")))
        ans.append(query(given_list))
    for i in ans:
        print(i)


if __name__ == "__main__":
    main()