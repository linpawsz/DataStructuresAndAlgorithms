# https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/


class Stack:
    def __init__(self):
        self.stack = []

    # Stack is empty when stack size is 0
    def isEmpty(self):
        return len(self.stack) == 0

    # Function to add an item to stack. It increases size by 1
    def push(self, item):
        self.stack.append(item)
        # print(str(item) + " pushed to stack ")

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

    # Function to insert_at_bottom recursive - just pop and push in the end
    def insert_at_bottom(self, x):
        if self.isEmpty():
            self.push(x)
        else:
            temp = self.pop()
            self.insert_at_bottom(x)
            self.push(temp)

    # Function to reverse recursive
    def reverse(self):
        if not self.isEmpty():
            temp = self.pop()
            self.reverse()
            self.insert_at_bottom(temp)


if __name__ == "__main__":
    stck = Stack()
    stck.push(10)
    stck.push(20)
    stck.push(30)
    stck.push(40)
    stck.reverse()

    print(stck.pop())
    print(stck.pop())
    print(stck.pop())
    print(stck.pop())
