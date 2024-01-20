class ListNode:
    def __init__(self, val = 0):
        self.val= val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next: #- check if the next attribute of the current node is not None. If the "current.next" is not None, it means there is another node after the current nodes, so the loop continues.
                current = current.next 
                #- The loop continues until the condition "current.next" became False (current.next = None), indicating that the current node is the last node in the linked list 
            current.next = new_node 
    
    def prepend(self, val):
        """Implement adding a new node at the beginning of the linked list
            Take a value as an input and creates a new node with that value, which becomes the new head of the list"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node 

    def pop(self):
        if self.head is None:
            raise IndexError('Linked list is empty')
        if self.head.next is None:
            #- If there is one node in the linked list, the head
            return self.head.val
        current = self.head
        previous = None #- keep track of the node before the current node during traversal

        while current.next:
            previous = current
            current = current.next
        
        popped_value = current.val
        previous.next = None #- disconnecting the last node from the linked list
        print(popped_value)

    def delete(self, val):
        """ Remove the first occurance of a node with the specified 'val' value from the linked list
            It traverses the list, searching for the nodes to delete
            If the node is found, it updates the 'next' attribute of the previous node to skip the node to be deleted """
        if self.head is None:
            return
        
        if self.head.val == val: #- the value to delete is the head node 
            self.head = self.head.next
            return 
        
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        """ Print the contents of the linked list. 
            It traverses the list from the head to the last node and prints the value of each node """
        if self.head is None:
            print('Linked list is empty')
        else:
            current = self.head
            while current:
                print(current.val, end = " ")
                current = current.next
            print() #- line break after printing the contents of the linked list

    def __iter__(self):
        """ Allow an object to be used in a 'for' loop or with the iter() function """
        current = self.head
        while current:
            yield current.val #- yield the value of each node in the linked list
            current = current.next

    def reverse(self):
        #- Initialize 2 pointers
        previous = None
        current = self.head

        #- Start a loop that continues until the 'current' pointer reaches the end of the linked list (i.e until current becomes None)
        while current:
            next_node = current.next #- Save the reference to the next node
            #- Update the 'next' pointer of the current node to point to the previous ndoe, effectively reversing the directioin of the next reference
            current.next = previous #- Reverse the next reference of the current node

            #- Move previous and current one step forward to continue traversing the linked list
            previous = current
            current = next_node

        self.head = previous #- update the head to the last node (new first node)
        return self
    
def add_two_number(l1, l2):
    result_head = ListNode(0) #- Head of the result linked list
    current = result_head #- Pointer to the current node in the result list
    carry  = 0 #- Carry value for addition

    while l1 or l2 or carry:
        value1 = l1.val if l1 else 0
        value2 = l2.val if l2 else 0

        #- Calculate the sum of the value and the carry
        total = value1 + value2 + carry
        carry = total // 10
        digit = total % 10

        #- Create a new node with the digit and add it to the result list 
        current.next = ListNode(digit)
        current = current.next

        #- Move to the next node in the input lists (if available)
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return result_head.next #- Return the head of the result list (excluding the dummy node )

    
my_list = LinkedList()
my_list.append(5)
my_list.append(10)
my_list.prepend(3)
my_list.append(15)

my_list.display()
l1 = my_list.reverse()


my_list1 = LinkedList()
my_list1.append(1)
my_list1.append(2)
my_list1.prepend(3)
my_list1.append(5)

my_list1.display()
l2 = my_list1.reverse()

add_two_number(l1,l2)





### IDEAS - EXPLAINATIONS

## def append:
# vòng lặp while để đảm bảo append sẽ thêm new node vào dưới nhất/tận cùng nhất của linked list chứ không phải append bưa bừa phứa hay append new node ở đầu list 

## def pop:
# - It is initialized as none before the loop starts because there is no previous node initially
# - As the loop iterates through the linked list, "previous" is updated to hold the reference to the ndoe that comes before the "current" node in each iteration
# - When the loop reaches the last node (i.e "current.next" is None), "previous" holds the reference to the node before the last node
# - To remove the last node, the line "previous.next = None" set the "next" attribute of the previous node to "None", effectively disconnecting the last node from the linked list 

## def reverse, the INTUITION
# - When reversing a linked list, the direction of the "next" pointer needs to be reversed 
# - To do this, we can iterate through the linked list, at each step, modify the next pointer of the current node to the previous one

### Đề bài:
# You re given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add two numbers and returns the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself