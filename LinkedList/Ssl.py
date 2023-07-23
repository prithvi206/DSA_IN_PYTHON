class Node:
    def __init__(self,value):
        self.value = value
        self.next =None

class Ssl:
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.length =0

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next= new_node
            self.tail= new_node
        self.length+=1

    def __str__(self):
        temp_node = self.head
        result =''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result+='->'
            temp_node = temp_node.next
        return result
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index-1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length+=1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while current :
            if current.value == target:
                return index
            current = current.next
            index+=1
        return -1
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length-=1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length-=1
        return popped_node
    
    def get(self, index):
        if index == -1:
            return self.tail
        if index <-1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set(self ,index,value):
        temp = self.get(index)
        if temp :
            temp.value = value
            return True
        return False
    
    def remove(self,index):
        if index >= self.length or index<0:
            return None
        if index == self.length-1:
            return self.pop()
        if index==0:
            return self.pop_first()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length-=1
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length =0

    def reverse(self):
        prev_node = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev_node
            prev_node= current
        self.head , self.tail = self.tail , self.head

    def middle(self):
        fast = self.head
        slow = self.head
        while fast is not None or fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def remove_duplicates(self):
        if self.head is None:
            return 
        node_values = set()
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:
                current_node.next= current_node.next.next
                self.length-=1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node

    





