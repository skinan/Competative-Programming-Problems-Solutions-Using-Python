# Hackerrank
# Practice > Python > Basic Data Types > Finding the percentage


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    temp = student_marks.get(query_name)
    ans =  sum(temp)/len(temp)
    print("{0:.2f}".format(ans))
