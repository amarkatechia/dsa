'''
Doubly linked list methods.
Assumes the class has: head, tail, length, and Node(value) with .value, .next, and .prev
'''

class Node:
    def __init__(self, value): 
        self.value = value
        self.next = None
        self.prev = None

'CONSTRUCTOR'
class DoublyLinkedList:
    def __init__(self, value):
       new_node = Node(value) #create the first node
       self.head = new_node #head points at the only node
       self.tail = new_node #tail points at the only node
       self.length = 1 #list starts with one node

'PRINT LIST'
def print_list(self):
    temp = self.head #start at the first node
    while temp is not None: #walk until we run out of nodes
        print(temp.value)
        temp = temp.next #move one step toward the tail

'APPEND LIST'
def append(self, value):
    new_node = Node(value) #node to add at the end
    if self.length is None: #if list is empty, new node is both head and tail
        self.head = new_node
        self.tail = new_node
    else: #if list has nodes, link new node after the current tail
        self.tail.next = new_node #old tail now points forward to the new node
        new_node.prev = self.tail #new node points back to the old tail
        self.tail = new_node #tail follows the new last node
    self.length += 1 #increment the length
    return True

'PREPEND LIST'
def prepend(self, value):
    new_node = Node(value) #node to add at the front
    if self.length == 0: #if list is empty, new node is both head and tail
        self.head = new_node
        self.tail = new_node
    else: #if list has nodes, link new node before the current head
        new_node.next = self.head #new node points forward to the old head
        self.head.prev = new_node #old head points back to the new node
        self.head = new_node #head now starts at the new node
    self.length += 1 #increment the length
    return True
    
'POP LIST'
def pop(self):
    if self.length == 0: #if list is empty, return None
        return None
    temp = self.tail
    if self.length == 1: #if list has only one node, set head and tail to None
        self.head = None
        self.tail = None
    else: #if list has more than one node, set tail to the previous node and set the next node to None
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None #set the previous node to None
    self.length -= 1 #decrement the length
    return temp #return the popped node

'POP FIRST LIST'
def pop_first(self):
    if self.length == 0: #if list is empty, return None
        return None
    temp = self.head
    if self.length == 1: #if list has only one node, set head and tail to None
        self.head = None
        self.tail = None
    else: #if list has more than one node, set head to the next node and set the previous node to None
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
    self.length -= 1 #decrement the length
    return temp #return the popped node

'GET LIST'
def get(self, index):
    if index < 0 or index >= self.length: #if index is out of bounds, return None
        return None
    temp = self.head
    if index < self.length / 2: #if index is in the first half of the list, start at the head
        for _ in range(index):
            temp = temp.next
    else: #if index is in the second half of the list, start at the tail
        temp = self.tail
        for _ in range(self.length - 1, index, -1):
            temp = temp.prev
    return temp #return the node at the index

'SET LIST'
def set_value(self, index, value):
    if index < 0 or index >= self.length: #if index is out of bounds, return False
        return False
    temp = self.get(index) #get the node at the index
    if temp: #if the node exists, set the value
        temp.value = value
        return True
    return False #if the node does not exist, return False

'INSERT LIST'
def insert(self, index, value):
    if index < 0 or index > self.length: #if index is out of bounds, return False
        return False
    if index == 0: #if index is 0, prepend the value
        return self.prepend(value)
    if index == self.length: #if index is the length of the list, append the value
        return self.append(value)
    new_node = Node(value) #create the new node
    before = self.get(index - 1) #get the node before the index
    after = before.next #get the node after the index
    new_node.prev = before #set the previous node to the node before the index
    new_node.next = after #set the next node to the node after the index
    before.next = new_node #set the next node to the new node
    after.prev = new_node #set the previous node to the new node
    self.length += 1 #increment the length
    return True

'REMOVE LIST'
def remove(self, index):
    if index < 0 or index >= self.length: #if index is out of bounds, return None
        return None
    if index == 0: #if index is 0, pop the first node
        return self.pop_first()
    if index == self.length - 1: #if index is the last node, pop the last node
        return self.pop()
    temp = self.get(index) #get the node at the index
    temp.next.prev = temp.prev #set the previous node to the node before the index
    temp.prev.next = temp.next #set the next node to the node after the index
    temp.next = None #set the next node to None
    temp.prev = None #set the previous node to None
    self.length -= 1 #decrement the length
    return temp #return the removed node

'''
DOUBLY LINKED LIST INTERVIEW QUESTIONS / LEETCODE PROBLEMS
'''

'PALINDROME CHECK'
def is_palindrome(self):
    # 1. If the length of the doubly linked list is 0 or 1, then 
    # the list is trivially a palindrome. 
    if self.length <= 1:
        return True
    
    # 2. Initialize two pointers: 'forward_node' starting at the head 
    # and 'backward_node' starting at the tail.
    forward_node = self.head
    backward_node = self.tail
    
    # 3. Traverse through the first half of the list. We only need to 
    # check half because we're comparing two nodes at once: one from 
    # the beginning and one from the end.
    for i in range(self.length // 2):
        # 3.1. Compare the values of 'forward_node' and 'backward_node'. 
        # If they're different, the list is not a palindrome.
        if forward_node.value != backward_node.value:
            return False
        
        # 3.2. Move the 'forward_node' one step towards the tail and 
        # the 'backward_node' one step towards the head for the next iteration.
        forward_node = forward_node.next
        backward_node = backward_node.prev
 
    # 4. If we've gone through the first half of the list without 
    # finding any non-matching node values, then the list is a palindrome.
    return True

'REVERSE LIST'
def reverse(self):
    # Initialize 'temp' to point to the list's head.
    # 'temp' is used to traverse the list.
    temp = self.head
    
    # Loop until 'temp' is None, signifying the
    # end of the list has been reached.
    while temp is not None:
        # Swap the current node's 'prev' and 'next'.
        # This reverses the link direction for the node.
        # 'prev' becomes 'next', and vice versa.
        temp.prev, temp.next = temp.next, temp.prev
        
        # Move to the next node in the original list
        # order to continue the reversal.
        # After swapping, 'prev' points to the next
        # node in original order, so move to 'temp.prev'.
        temp = temp.prev
        
    # After reversing all nodes, update the list's
    # head and tail to reflect the new order.
    # The original head is now the tail, and the
    # original tail is now the head.
    self.head, self.tail = self.tail, self.head

'PARTITION LIST'
def partition_list(self, x):
    # If the list is empty, return immediately
    # Nothing to partition
    if not self.head:
        return None
 
    # Create two dummy nodes to serve as the starting
    # points for the two new partitions
    # dummy1 → nodes with values < x
    # dummy2 → nodes with values ≥ x
    dummy1 = Node(0)
    dummy2 = Node(0)
 
    # prev1 tracks the end of the < x partition
    # prev2 tracks the end of the ≥ x partition
    prev1 = dummy1
    prev2 = dummy2
 
    # Start at the head of the original list
    current = self.head
 
    # Traverse the original list and divide nodes
    # into two separate partitions based on their value
    while current:
        if current.value < x:
            # Append current node to the < x list
            # Update pointers to maintain .next/.prev
            prev1.next = current
            current.prev = prev1
            prev1 = current
        else:
            # Append current node to the ≥ x list
            # Update pointers to maintain .next/.prev
            prev2.next = current
            current.prev = prev2
            prev2 = current
 
        # Move to the next node in the original list
        current = current.next
 
    # Terminate the ≥ x list to prevent cycle or
    # trailing data from previous .next values
    prev2.next = None
 
    # Connect the two partitions:
    # Link the end of the < x list to the beginning
    # of the ≥ x list
    prev1.next = dummy2.next
 
    # If the ≥ x list has at least one node,
    # update its .prev to point to the < x list
    if dummy2.next:
        dummy2.next.prev = prev1
 
    # Update the head of the list to the start of
    # the < x partition (after dummy1)
    self.head = dummy1.next
 
    # Ensure the new head has no previous pointer (important for DLL structure)
    self.head.prev = None

'REVERSE BETWEEN'
def reverse_between(self, start_index, end_index):
    # Reverses the portion of the list between the
    # given start_index and end_index in-place.
    # Assumes 0-based indexing.
 
    # If the list has 0 or 1 nodes, or no change needed
    if self.length <= 1 or start_index == end_index:
        return
 
    # Create a dummy node before head to simplify edge cases
    dummy = Node(0)
    dummy.next = self.head
    self.head.prev = dummy
 
    # Traverse to the node just before the start_index
    prev = dummy
    for _ in range(start_index):
        prev = prev.next
 
    # current points to the first node in the segment to reverse
    current = prev.next
 
    # Reverse the segment using node splicing
    for _ in range(end_index - start_index):
        node_to_move = current.next
 
        # Detach node_to_move from its current position
        current.next = node_to_move.next
        if node_to_move.next:
            node_to_move.next.prev = current
 
        # Insert node_to_move right after prev
        node_to_move.next = prev.next
        prev.next.prev = node_to_move
        prev.next = node_to_move
        node_to_move.prev = prev
 
    # Update head pointer in case it was changed
    self.head = dummy.next
    self.head.prev = None

'SWAP NODES IN PAIRS'
def swap_pairs(self):
    # Step 1: Initialize a dummy node to act as a placeholder
    # for the start of the list.
    dummy_node = Node(0)
 
    # Connect this dummy node to the actual head of the list.
    # This simplifies the swapping process.
    dummy_node.next = self.head
 
    # Step 2: Initialize 'previous_node' to 'dummy_node'.
    # This helps us remember the node just before the pair
    # we are about to swap.
    previous_node = dummy_node
 
    # Step 3: Loop through the list as long as there are pairs
    # of nodes available to swap.
    while self.head and self.head.next:
 
        # Identify the first node in the pair to be swapped.
        first_node = self.head
 
        # Identify the second node in the pair to be swapped.
        second_node = self.head.next
 
        # Update 'previous_node' to point to 'second_node',
        # effectively skipping over 'first_node'.
        previous_node.next = second_node
 
        # Connect 'first_node' to the node that comes after
        # 'second_node'. This ensures we don't lose the
        # rest of the list.
        first_node.next = second_node.next
 
        # Swap 'first_node' and 'second_node' by connecting
        # 'second_node' back to 'first_node'.
        second_node.next = first_node
 
        # Update the 'prev' pointers for both 'first_node'
        # and 'second_node' to maintain the doubly-linked
        # structure.
        second_node.prev = previous_node
        first_node.prev = second_node
 
        # If there's a node after 'first_node', update its
        # 'prev' to point back to 'first_node'.
        if first_node.next:
            first_node.next.prev = first_node
 
        # Move the 'head' to the node just after 'first_node'
        # to prepare for the next iteration.
        self.head = first_node.next
 
        # Update 'previous_node' to point to 'first_node'
        # for the next pair to swap.
        previous_node = first_node
 
    # After the loop, set the new head of the list to the
    # node that comes after 'dummy_node'.
    self.head = dummy_node.next
 
    # Make sure the new head's 'prev' is set to None, as it
    # is now the first node in the list.
    if self.head:
        self.head.prev = None