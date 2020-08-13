r,c = int(input()),int(input())
m = [[0 for x in range(r+1)] for y in range(c+1)]
t = 0
j = 0
i = 0
def matrix():
    for i in range(0,r):
        s = input()
        l = list(s)
        length = len(l)
        for j,t in zip(range(r+1),range(length)):
            m[i][j] = l[t]
            j = j + 1
            t = t + 1
matrix()
n = [[0 for x in range(r+1)] for y in range(c+1)]
def number():
    no = 0
    for i in range(0,r):
        for j in range(0,c):
            if i == 0:
                if m[i][j] != '*':
                    no = no + 1
                    n[i][j] = no
            else:
                if m[i][j] != '*' and ( m[i][j-1] == '*' or m[i-1][j] == '*'or j == 0):
                    no = no + 1
                    n[i][j] = no
number()
def across():
    print("puzzle#1")
    print("Across")
    s = ""
    for i in range(0,r):
        for j in range(0,c):
            if m[i][j] != '*':
                s = s+str(m[i][j])
            if m[i][j] == '*' or j == c-1: 
                if m[i][j] == '*' and m[i][j-1] != '*' and j != 0 and j != c-1:
                    print(str(n[i][j-len(s)])+'.'+s)
                    s = ""
                if j == c-1 and m[i][j] != '*':
                    j = j+1
                    print(str(n[i][j-len(s)])+'.'+s)
                    s=""
                if j == c-1 and m[i][j] == '*' and m[i][j-1] != '*':
                    print(str(n[i][j-len(s)])+'.'+s)
                    s = ""
across()
def down():
    print("Down")
    j = 0
    s = ""
    d = {}
    for j in range(0,c):
        for i in range(0,r):
            if m[i][j] != '*':
                s =s+str(m[i][j])
            if (m[i][j] == '*' and i != 0) or i == r-1:
                if m[i][j] == '*' and m[i-1][j] != '*' and i != r-1:
                    d[n[i-len(s)][j]] = s
                    s = ""
                if i == r-1 and m[i][j] != '*':
                    i = i+1
                    d[n[i-len(s)][j]] = s
                    s = ""
                if i == r-1 and m[i][j] == '*' and m[i-1][j] != '*':
                    d[n[i-len(s)][j]] = s
                    s = ""
    l1 = d.keys()
    for key in sorted(l1):
        print("%s.%s"%(key,d[key]))
down()
