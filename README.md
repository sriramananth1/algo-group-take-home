# Algo Group Takehome Assignment - Sriram Ananthakrishnan

Implemented the stack, with testcases at the bottom of the option2.py file.

Since we aren't allowed to use any built-in datastructures, I used a linked list to implement the stack. Specifically, we initialize the stack with a tail pointer set to None and a length set to 0. We use a tail pointer to denote the top of the stack to make all operations O(1).

When pushing a node, it suffices to create a new node object and point it to the tail of the linked list, then set the stack to this new node. When popping, it suffices to look at the tail node, set the stack equal to tail.next, and return the value of the tail node. Likewise, when peeking, we simply return the value of the tail node. Finally, we store the length variable that updates on every operation.

# Test Cases:

Test 1: All outputs match
Test 2: All outputs match
Test 3: All outputs match



