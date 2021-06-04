# From https://www.geeksforgeeks.org/linked-list-set-1-introduction/
# https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
# Advantages over arrays
# 1) Dynamic size
# 2) Ease of insertion/deletion
# Drawbacks:
# 1) Random access is not allowed. We have to access elements sequentially starting from the first node.
# So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here.
# 2) Extra memory space for a pointer is required with each element of the list.
# 3) Not cache friendly. Since array elements are contiguous locations, there is locality of reference
# which is not there in case of linked lists.
# This is for quick reference only - not meant for any other use!
# Figure out the logic on the functions again - revise


# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null


# Linked List class
class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    # Traverse the Linked List
    def printList(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)

    # Add a new element in the start of the list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new element after a prev_node in the list
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            return
        temp = self.head
        while temp != prev_node:
            temp = temp.next
        new_node = Node(new_data)
        new_node.next = temp.next
        prev_node.next = new_node

    # Append a new element at the end of the list
    def append(self, new_data):
        new_node = Node(new_data)
        # Check to see if LL is empty - then assign the element in the start itself
        if self.head is None:
            self.head = new_node
            return
        # Otherwise traverse the LL to the last element
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Delete an element who's data matches key
    def deleteNode(self, key):
        temp = self.head

        # Edge case #1 - head node has the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Edge Case #2 - let's traverse this LL and check for the key
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Edge Case #3 - key is not present in the list - we reached the end of the list
        if temp is None:
            return

        # Only on edge case #2 do we reach here - so we can write this prev.next statement
        prev.next = temp.next
        temp = None

    # Delete a node at a certain position(int)
    def deleteNode_position(self, position):

        # Edge Case #1 - if we don't have the LL itself and it's empty - return
        if self.head is None:
            return

        temp = self.head

        # If the position is the first element - the head
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Iterate to the position - we don't do checks with key - just iterate to position
        for i in range(position -1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    # Reverse the LL and switch the connection between the nodes
    def reverse(self, head):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == '__main__':
    # Initialize the Linked List
    llist = LinkedList()
    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # Make connections between nodes
    # llist.head.next = second
    # second.next = third

    # Use the linked list operations and test them out
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insertAfter(llist.head.next, 8)
    llist.deleteNode(7)
    # llist.deleteNode_position(3)

    # Traverse the Linked List
    llist.printList()

    # Reverse the LL tryout - that worked
    llist.reverse(llist.head)

    llist.printList()
