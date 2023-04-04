class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next

def combine_lists(l1, l2):
    combined_list = LinkedList()
    temp_dict = {}
    current_node = l1.head
    while current_node is not None:
        if current_node.data not in temp_dict:
            combined_list.add_node(current_node.data)
            temp_dict[current_node.data] = 1
        current_node = current_node.next

    current_node = l2.head
    while current_node is not None:
        if current_node.data not in temp_dict:
            combined_list.add_node(current_node.data)
            temp_dict[current_node.data] = 1
        current_node = current_node.next

    return combined_list

# Test the solution
l1 = LinkedList()
l1.add_node(1)
l1.add_node(2)
l1.add_node(3)
l1.add_node(4)

l2 = LinkedList()
l2.add_node(3)
l2.add_node(4)
l2.add_node(5)
l2.add_node(6)

combined_list = combine_lists(l1, l2)
combined_list.print_list() # Output: 1 2 3 4 5 6
