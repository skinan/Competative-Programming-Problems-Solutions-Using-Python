# Codeforces
# Codeforces Round #590 (Div. 3)
# B2. Social Network (hard version)
# Problem Statement Link : https://codeforces.com/contest/1234/problem/B2


from collections import deque


def main():
    n, k = map(int, input().split(" "))
    given_list = list(map(int, input().split(" ")))

    main_list = deque()
    s = set()

    for i in given_list:
        if len(main_list) < k:
            if i in s:
                continue

            main_list.appendleft(i)
            s.add(i)

        elif len(main_list) == k:
            if i in s:
                continue

            s.discard(main_list.pop())
            main_list.appendleft(i)
            s.add(i)

    # Print Answers
    print(len(main_list))
    print(*main_list)


if __name__ == "__main__":
    main()
