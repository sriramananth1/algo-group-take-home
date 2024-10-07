# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values


class Node:
    def __init__(self, val, next = None): # assign self.next to next
        self.val = val
        self.next = None
    


class IntStack:
    
    def __init__(self, tail = None, len = 0):
        self.tail = None
        self.len = 0
    
    def push(self, val : int):
        #adds val to end of linked list
        node = Node(val)
        self.len += 1
        if not self.tail:
            self.tail = node
            return
     
        node.next = self.tail #points node to tail
        self.tail = node  #sets tail to nod

    
    def peek(self):
        #returns final element 
       
        if not self.tail:
            raise Exception("Stack is emtpy")
        return self.tail.val

    
    def pop(self):
        #removes final element from linked list
        
        if not self.tail:
            raise Exception("Stack is empty")
        fin = self.tail.val 
        self.len -= 1
        prev = self.tail.next
        self.tail = prev
        return fin

    def size(self):
        return self.len
    


'''
Test 1:
'''
print('''Test 1. Expected Outputs:
4
2
5
4
-----------------------------------------
Actual Outputs: ''')
s = IntStack()
s.push(4)
print(s.peek()) #4
s.push(5)
print(s.size()) #2 
print(s.peek()) #5
s.pop()
print(s.peek()) #4 

'''
Test 2:
'''
print('''Test 2. Expected Outputs:
3
1
-----------------------------------------
Actual Outputs: ''')
s = IntStack()
s.push(8)
s.push(37)
s.push(48)
print(s.size()) #3
s.pop()
s.pop()
print(s.size()) #1

'''
Test 3:
'''
print('''Test 3. Expected Outputs:
99 99
98 98
97 97
96 96
95 95
94 94
93 93
92 92
91 91
90 90
89 89
88 88
87 87
86 86
85 85
84 84
83 83
82 82
81 81
80 80
79 79
78 78
77 77
76 76
75 75
74 74
73 73
72 72
71 71
70 70
69 69
68 68
67 67
66 66
65 65
64 64
63 63
62 62
61 61
60 60
59 59
58 58
57 57
56 56
55 55
54 54
53 53
52 52
51 51
50 50
49 49
48 48
47 47
46 46
45 45
44 44
43 43
42 42
41 41
40 40
39 39
38 38
37 37
36 36
35 35
34 34
33 33
32 32
31 31
30 30
29 29
28 28
27 27
26 26
25 25
24 24
23 23
22 22
21 21
20 20
19 19
18 18
17 17
16 16
15 15
14 14
13 13
12 12
11 11
10 10
9 9
8 8
7 7
6 6
5 5
4 4
3 3
2 2
1 1
1 1
0 None
-----------------------------------------
Actual Outputs: ''')

s = IntStack()
for i in range(100):
    s.push(i+1)

for j in range(100):
    s.pop()
    print(s.size(), s.peek())
    
