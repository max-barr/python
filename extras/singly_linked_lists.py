class SLList:
    def __init__(self):
        self.head = None
    
    # Add a new node to the front of the list
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    # Traverse through the list
    def print_values(self):
        # A pointer to the list's first node
        current = self.head
        # While runner exists (runner != None)
        while current:
            print(current.value)
            current = current.next
        return self

    # Traverse through the list and adding a value to the end
    def add_to_back(self, val):
        # Edge case: If the list is empty we use add to front method
        if self.head == None:
            self.add_to_front(val)
            return self
        # Else:
        new_node = SLNode(val)
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = new_node
        return self

    # Remove the node at the front of the list
    def remove_from_front(self):
        if self.head != None:
            self.head = self.head.next
        return self

    # Remove the node at the back of the list
    def remove_from_back(self):
        # Empty list
        if self.head == None:
            return self
        # One node in the list
        elif self.head.next == None:
            self.head = None
            return self
        # At least 2 nodes in the list
        else: 
            current = self.head
            while (current.next.next != None):
                current = current.next
            current.next = None
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SLList()
# my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.add_to_front("B").add_to_front("A").add_to_back("C").add_to_back("Z").add_to_back("Y").remove_from_back().remove_from_back().print_values()