class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        found = False
        
        if target < self.value:
            if self.left is None:
                return False
            found = self.left.contains(target)
            
        if target > self.value:
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
           return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
            
        if self.right:
            self.right.for_each(fn)

    # Print all the values in order from low to high
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
            
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        
        while len(queue) > 0:
            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)

            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)


# Import Node, LinkedList, Queue, and Stack Classes
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def __str__(self):
        output = ""
        current_node = self.head
        while current_node is not None:
            output += f"{current_node.value}"
            # Update the tracker node to the next node
            current_node = current_node.next_node
        return output

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
          new_node.next_node = self.head 
          self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def get_list_size(self):
        i = 0
        current_item = self.head
        if not current_item:
            return i
        while current_item is not None:
            i += 1
            current_count = i
            current_item = current_item.next_node
        return current_count

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            node = self.storage.remove_head()
            return node
        return None

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            node = self.storage.remove_head()
            return node
        return None
