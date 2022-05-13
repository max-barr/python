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
        runner = self.head
        # While runner exists (runner != None)
        while runner:
            print(runner.value)
            runner = runner.next
        return self

    # Traverse through the list and adding a value to the end
    def add_to_back(self, val):
        # Edge case: If the list is empty we use add to front method
        if self.head == None:
            self.add_to_front(val)
            return self
        # Else:
        new_node = SLNode(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SLList()
# my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.add_to_front("B").add_to_front("A").print_values()