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


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.peek())
    s.pop()
    print(s.peek())