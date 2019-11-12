# Project Euler #25: N-digit Fibonacci number
# Hackerrank Contest: ProjectEuler + 
# Dynamic Programming
# Time Complexity : O(n)


def find(m, ans):
    c = 1  # For length check
    f = 0  # First Number
    s = 1  # Second Number
    n = 1  # Next Number 
    i = 2  # To track N th Fibonocci Number
    
    # Loop to generate fibanocci number and store answers.
    while len(str(n)) <= m:
     
        n = f + s
        
        if c == len(str(n)): # Keep storing answers.(Memoization)
            ans.append(i)  
            c += 1
           
        f, s = s, n
        i += 1 
 

def main():
    query = []
    for _ in range(int(input())):
        query.append(int(input()))
    
    m = max(query)  # Find The maximum length of digit ee need to find.
    
    ans = []  # Maintain an array to store results.
    find(m, ans)
    # Finally print the desired query results from array.
    for i in query:
        print(ans[i - 1])


if __name__ == "__main__":
    main()
