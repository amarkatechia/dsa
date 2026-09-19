'''
Singly linked list methods.
Assumes the class has: head, tail, length, and Node(value) with .value and .next
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

'''CONSTRUCTOR'''
def __init__(self):
    self.head = None
    self.tail = None
    self.length = 1 #initialize with a node

'''PRINT LIST'''
def print_list(self) :
    # Start at the first node and walk until we run out of nodes
    temp = self.head
    while temp is not None:
        print (temp. value)
        temp = temp. next  # move one step toward the end

'''APPEND LIST'''
def append (self, value):
    # Add a node at the end. O(1) because we keep a tail pointer.
    new_node = Node(value)
    if self.length == 0:
        # Empty list: the new node is both first and last
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node  # old last node now points at the new one
        self.tail = new_node       # tail follows the new last node
    self.length += 1  # increment once (not also inside the empty branch)

'''PREPEND LIST'''
def prepend(self, value):
    # Add a node at the front. O(1).
    new_node = Node(value)
    if self.length == 0:
        # Empty list: new node is both head and tail
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head  # new node points at the old first node
        self.head = new_node       # head now starts at the new node
    self.length += 1
    return True

'''POP LIST'''
def pop(self):
    # Remove and return the last node. O(n): we walk from head to find the new tail.
    if self.length == 0:
        return None
    temp = self.head  # will land on the last node (the one we remove)
    pre = self.head   # will land on the node before last (the new tail)
    while temp.next is not None:
        pre = temp
        temp = temp.next
    self.tail = pre          # second-to-last becomes the last node
    self.tail.next = None    # unlink the removed node from the list
    self.length -= 1
    if self.length == 0:
        # We just removed the only node; head and tail must both be empty
        self.head = None
        self.tail = None
    return temp

'''POP FIRST LIST'''
def pop_first(self):
    # Remove and return the first node. O(1).
    if self.length == 0:
        return None
    temp = self.head              # node we are removing
    self.head = self.head.next    # list now starts at the second node
    temp.next = None              # detach the removed node from the rest
    self.length -= 1
    if self.length == 0:
        # Removed the only node; tail still pointed at it
        self.tail = None
    return temp

'''GET LIST'''
def get(self, index):
    # Return the node at index, or None if index is out of range. O(n).
    if index < 0 or index >= self.length:
        return None
    temp = self.head
    for _ in range(index):
        temp = temp.next  # walk index steps from the head
    return temp

'''SET LIST'''
def set_value(self, index, value):
    # Change the value of the node at index. Reuses get().
    temp = self.get(index)
    if temp:
        temp.value = value
        return True
    return False  # index was invalid

'''INSERT LIST'''
def insert(self, index, value):
    # Insert a new node at index. Index == length means append at the end.
    if index < 0 or index > self.length:
        return False  # note: index == length is allowed (append)
    if index == 0:
        return self.prepend(value)  # reuse front-insert so head stays correct
    if index == self.length:
        return self.append(value)   # reuse end-insert so tail stays correct
    new_node = Node(value)
    temp = self.get(index - 1)      # node that will sit just before the new one
    new_node.next = temp.next       # new node points at the old occupant of index
    temp.next = new_node            # previous node now points at the new node
    self.length += 1
    return True

'''REMOVE LIST'''
def remove(self, index):
    # Remove and return the node at index.
    if index < 0 or index >= self.length:
        return None
    if index == 0:
        return self.pop_first()     # keeps head (and empty-list tail) correct
    if index == self.length - 1:
        return self.pop()           # keeps tail correct
    prev = self.get(index - 1)      # node before the one we remove
    temp = prev.next                # node we remove
    prev.next = temp.next           # skip over temp
    temp.next = None                # detach the removed node
    self.length -= 1
    return temp

'''REVERSE LIST'''
def reverse(self):
    # Reverse the list in place by flipping every next pointer. O(n).
    temp = self.head
    self.head = self.tail  # after reverse, old last node is first
    self.tail = temp       # old first node is last
    after = temp.next      # node after temp (will be overwritten in the loop)
    before = None          # node that should sit behind temp after the flip
    for _ in range(self.length):
        after = temp.next     # save the next node before we overwrite temp.next
        temp.next = before    # reverse this link: point backward
        before = temp         # slide the "already reversed" window forward
        temp = after          # move to the next original node


'''
SINGLY LINKED LIST INTERVIEW QUESTIONS / LEETCODE PROBLEMS
'''

'''FIND THE MIDDLE NODE'''
def find_middle_node(self):
    # 1. Initialize two pointers: 'slow' and 'fast', 
    # both starting from the head.
    slow = self.head
    fast = self.head
 
    # 2. Iterate as long as 'fast' pointer and its next 
    # node are not None.
    # This ensures we don't get an error trying to access
    # a non-existent node.
    while fast is not None and fast.next is not None:
        
        # 2.1. Move 'slow' one step ahead.
        # This covers half the distance that 'fast' covers.
        slow = slow.next
        
        # 2.2. Move 'fast' two steps ahead.
        # Thus, when 'fast' reaches the end, 'slow' 
        # will be at the middle.
        fast = fast.next.next
 
    # 3. By now, 'fast' has reached or surpassed the end, 
    # and 'slow' is positioned at the middle node.
    # Return the 'slow' pointer, which points to 
    # the middle node.
    return slow

'''HAS LOOP'''
def has_loop(self):
    # 1. Initialize two pointers: 'slow' and 'fast', 
    # both starting from the head.
    slow = self.head
    fast = self.head
 
    # 2. Continue traversal as long as the 'fast' pointer 
    # and its next node aren't None.
    # This ensures we don't run into errors trying to 
    # access non-existent nodes.
    while fast is not None and fast.next is not None:
        
        # 2.1. Move 'slow' pointer one step ahead.
        slow = slow.next
        
        # 2.2. Move 'fast' pointer two steps ahead.
        fast = fast.next.next
        
        # 2.3. Check for cycle: If 'slow' and 'fast' meet,
        # it means there's a cycle in the linked list.
        if slow == fast:
            # 2.3.1. If they meet, return True 
            # indicating the list has a loop.
            return True
 
    # 3. If we've gone through the entire list and 
    # the pointers never met, then the list doesn't have a loop.
    return False

'''FIND KTH NODE FROM THE END'''
def find_kth_from_end(ll, k):
    # 1. Initialize two pointers, 'slow' and 'fast', both pointing to the 
    # starting node of the linked list.
    slow = fast = ll.head   
    
    # 2. Move the 'fast' pointer 'k' positions ahead.
    for _ in range(k):
        # 2.1. If at any point during these 'k' movements, the 'fast' 
        # pointer reaches the end of the list, then it means the list 
        # has less than 'k' nodes, and thus, returning None is appropriate.
        if fast is None:
            return None
        
        # 2.2. Move the 'fast' pointer to the next node.
        fast = fast.next
 
    # 3. Now, move both 'slow' and 'fast' pointers one node at a time until 
    # the 'fast' pointer reaches the end of the list. Since the 'fast' pointer 
    # is already 'k' nodes ahead of the 'slow' pointer, by the time 'fast' 
    # reaches the end, 'slow' will be at the kth node from the end.
    while fast:
        slow = slow.next
        fast = fast.next
        
    # 4. Return the 'slow' pointer, which is now pointing to the kth node 
    # from the end.
    return slow

'''REMOVE DUPLICATES'''
# USING SETS
def remove_duplicates(self):
    # 1. Initialize a set called 'values' to store unique node values.
    values = set()
    
    # 2. Initialize 'previous' to None. 
    # This will point to the last node we've seen that had a unique value.
    previous = None
    
    # 3. Start at the head of the linked list.
    current = self.head
 
    # 4. Traverse through the linked list.
    while current:
        # 4.1. Check if the value of the current node is already in the set.
        if current.value in values:
            # 4.1.1. If yes, bypass this node by pointing the next of 
            # 'previous' to the next of 'current'.
            previous.next = current.next
            
            # 4.1.2. Decrement the length of the list.
            self.length -= 1
        else:
            # 4.2. If not, add the value to the set.
            values.add(current.value)
            
            # 4.2.1. Update the 'previous' to point to 'current' now.
            previous = current
 
        # 4.3. Move to the next node in the list.
        current = current.next

#USING NESTED LOOPS
def remove_duplicates(self):
    # Start 'current' at the head node to check each
    # node’s value for duplicates in the linked list.
    current = self.head
    
    # Loop until 'current' is None (end of the list).
    # This visits every node to check for duplicates.
    while current:
        # 'runner' starts at 'current' to scan nodes
        # after it, looking for duplicate values.
        runner = current
        
        # Loop while 'runner.next' exists to check the
        # next node’s value against 'current’s value.
        while runner.next:
            # If the next node’s value equals 'current’s,
            # it’s a duplicate and needs to be removed.
            if runner.next.value == current.value:
                # Skip the duplicate by linking 'runner’s
                # next pointer to the node after it.
                runner.next = runner.next.next
                # Decrease the list length by 1 since we
                # removed a node.
                self.length -= 1
            else:
                # If no duplicate, move 'runner' to the
                # next node to keep checking.
                runner = runner.next
        
        # Move 'current' to the next node to check for
        # duplicates of its value in later nodes.
        current = current.next

'''BINARY TO DECIMAL'''
def binary_to_decimal(self):
    # 1. Initialize a variable 'num' to 0. This will be used to accumulate the 
    # decimal value as we traverse the linked list.
    num = 0
    
    # 2. Start at the head of the linked list.
    current = self.head
 
    # 3. Traverse through the linked list.
    while current:
        # 3.1. For each node, left shift the accumulated value by 1 position. 
        # This is the same as multiplying by 2. This step ensures that we are 
        # moving to the next binary position.
        # 
        # Example: If num is '10' (binary for 2) and next node value is '1', 
        # left shifting '10' results in '100' (binary for 4). 
        # Now, adding the next node value gives '101' (binary for 5).
        num = num * 2
        
        # 3.2. Add the current node's value (which should be either 0 or 1) 
        # to the accumulated value 'num'.
        num = num + current.value
        
        # OR both the above steps can be combined as:
        # num = num * 2 + current.value
        
        # 3.3. Move to the next node in the list.
        current = current.next
 
    # 4. Return the accumulated decimal value.
    return num

'''PARTITION LIST'''
def partition_list(self, x):
    # Check if list is empty
    # Return None if no nodes exist
    if not self.head:
        return None
 
    # Create dummy node for < x list
    dummy1 = Node(0)
    # Create dummy node for >= x list
    dummy2 = Node(0)
    # Pointer to last node in < x list
    prev1 = dummy1
    # Pointer to last node in >= x list
    prev2 = dummy2
    # Pointer to traverse original list
    current = self.head
 
    # Traverse the entire list
    while current:
        # If node value is less than x
        if current.value < x:
            # Link node to < x list
            prev1.next = current
            # Update last node in < x list
            prev1 = current
        # If node value is >= x
        else:
            # Link node to >= x list
            prev2.next = current
            # Update last node in >= x list
            prev2 = current
        # Move to next node
        current = current.next
 
    # Connect < x list to >= x list
    prev1.next = dummy2.next
    # Terminate the >= x list
    prev2.next = None
 
    # Set head to start of < x list
    self.head = dummy1.next

'''REVERSE BETWEEN'''
def reverse_between(self, start_index, end_index):
    # 1. Edge Case: If list has only one node or none, exit.
    if self.length <= 1:
        return
 
    # 2. Create a dummy node to simplify head operations.
    dummy_node = Node(0)
    dummy_node.next = self.head
 
    # 3. Init 'previous_node', pointing just before reverse starts.
    previous_node = dummy_node
 
    # 4. Move 'previous_node' to its position.
    # It'll be at index 'start_index - 1' after this loop.
    for i in range(start_index):
        previous_node = previous_node.next
 
    # 5. Init 'current_node' at 'start_index', start of reversal.
    current_node = previous_node.next
 
    # 6. Begin reversal:
    # Loop reverses nodes between 'start_index' and 'end_index'.
    for i in range(end_index - start_index):
        # 6.1. 'node_to_move' is next node we want to reverse.
        node_to_move = current_node.next
 
        # 6.2. Disconnect 'node_to_move', point 'current_node' after it.
        current_node.next = node_to_move.next
 
        # 6.3. Insert 'node_to_move' at new position after 'previous_node'.
        node_to_move.next = previous_node.next
 
        # 6.4. Link 'previous_node' to 'node_to_move'.
        previous_node.next = node_to_move
 
    # 7. Update list head if 'start_index' was 0.
    self.head = dummy_node.next

'''SWAP NODES IN PAIRS'''
def swap_pairs(self):
    # Create a dummy node to simplify head swaps
    dummy = Node(0)
    # Link dummy to the head of the list
    dummy.next = self.head
    # Set previous to dummy, before the pair
    previous = dummy
    # Set first to head, first node of pair
    first = self.head
 
    # Loop while there are two nodes to swap
    while first and first.next:
        # Second is the next node, pair's second
        second = first.next
 
        # Swap the pair:
        # Link previous to second (e.g., to 2)
        previous.next = second
        # Link first to node after second
        first.next = second.next
        # Link second to first to finish swap
        second.next = first
 
        # Update pointers for next pair:
        # Move previous to first (now second)
        previous = first
        # Move first to next node to process
        first = first.next
 
    # Set head to new first node after swaps
    self.head = dummy.next
