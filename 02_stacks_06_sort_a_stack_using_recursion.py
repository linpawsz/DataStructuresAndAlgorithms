# https://www.geeksforgeeks.org/sort-a-stack-using-recursion/

from sys import maxsize


class Stack:
    def __init__(self):
        self.stack = []

    # Stack is empty when stack size is 0
    def isEmpty(self):
        return len(self.stack) == 0

    # Function to add an item to stack. It increases size by 1
    def push(self, item):
        self.stack.append(item)
        print(str(item) + " pushed to stack ")

    # Function to remove an item from stack. It decreases size by 1
    def pop(self):
        if len(self.stack) == 0:
            return str(-maxsize - 1)  # return minus infinite
        return self.stack.pop()

    # Function to return the top from stack without removing it
    def peek(self):
        if len(self.stack) == 0:
            return str(-maxsize - 1)  # return minus infinite
        return self.stack[len(self.stack) - 1]

    def sortedInsert(self, element):
        if len(self.stack) == 0 or element > self.stack[-1]:
            self.stack.append(element)
        else:
            temp = self.stack.pop()
            self.sortedInsert(element)
            self.stack.append(temp)

    def sortStack(self):
        if len(self.stack) != 0:
            temp = self.stack.pop()
            self.sortStack()
            self.sortedInsert(temp)

    def printStack(self):
        for i in self.stack[::-1]:
            print(i, end = " ")
        print()


if __name__ == "__main__":
    stck = Stack()
    stck.push(30)
    stck.push(-5)
    stck.push(18)
    stck.push(14)
    stck.push(-3)

    stck.printStack()

    stck.sortStack()

    print("After sorting (top to bottom): ")
    stck.printStack()




