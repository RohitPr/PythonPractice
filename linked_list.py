class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self, data):
        return "<Node Data: %s>" % self.data


class LinkedList:

    def __init__(self):
        self.head = None
        self.next_node = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            current = self.next_node
            count += 1
        return count

    def add(self, data):
        """
        Adds a New Node at the start of the Linked List
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
