
class Node(object):
    
    def __init__(self, data=None):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data
   
    @data.setter
    def data(self,value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self,value):
        self._next = value
    
    
class SinglyLinkedList(object):
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._num_nodes = 0
        
    def __str__(self):
        if self.empty():
            return "[]"
        else:
            tmp_list = []  # Temporary list of strings
            cur = self._head            
            while cur != None:
                tmp_list.append("[%s]"%(cur.data))
                cur = cur.next
        
            return "->".join(tmp_list)
        
    def __len__(self):
         return self._num_nodes
            
    def empty(self):
        if self._num_nodes == 0:
            return True
        else:
            return False
        
    def insert(self, i, data):
        if i < 0 or i > self._num_nodes:
            raise IndexError("Index Error")
       
        node = Node(data)
        if self.empty():
            node.next = self._head
            self._head = node
            self._tail = self._head
           
        elif i == 0:
            node.next = self._head
            self._head = node
           
        elif i == self._num_nodes:
            self._tail.next = node
            self._tail = node
       
        else:
            pre = self._head
            for k in range (i - 1):
                pre = pre.next
            aft = pre.next
            node.next = aft
            pre.next = node
       
        self._num_nodes += 1

    def remove(self, i):
        if i < 0 or i > self._num_nodes:
            raise IndexError("Index Error")
           
        if self.empty():
            return
       
        else:
            if self._num_nodes == 1:
                self._head = None
                self._tail = None
           
            elif i == 0:
                node = self._head
                self._head = self._head.next
                del node
               
            elif i == self._num_nodes - 1:
                pre = self._head
                node = self._head.next
                while node.next != None:
                    pre = pre.next
                    node = node.next
                pre.next = None
                del node
                self._tail = pre
               
            else:
                pre = self._head
                for k in range (i-1):
                    pre = pre.next
                node = pre.next
                aft = node.next
                pre.next = aft
                del node
               
            self._num_nodes -= 1

              
    def clear(self):
        if self.empty():
            return
       
        else:
            for i in range(self._num_nodes - 2):
                self._head.next = None
            self._head = None
            self._tail = None
            self._num_nodes = 0
    
    def get(self, i):
        if i < 0 or i > self._num_nodes - 1:
            raise IndexError("Index Error")
        node = self._head
        for k in range (i):
            node = node.next
        return node.data

    
    def pop(self, i=None):
        if self.empty():
            raise IndexError("Index Error")
           
        node = self._head

    
    def search(self, target, start=0):
        if self._num_nodes == 1:
                self._tail = None
               
            else:
                pre = self._head
                node = self._head.next
                while node.next != None:
                    pre = pre.next
                    node = node.next
                pre.next = None
                self._tail = pre
               
        else:
            if self._num_nodes == 1:
                self._tail = None
           
            elif i == 0:
                self._head = self._head.next
               
            elif i == self._num_nodes - 1:
                pre = self._head
                node = self._head.next
                while node.next != None:
                    pre = pre.next
                    node = node.next
                pre.next = None
                self._tail = pre
               
            else:
                pre = self._head
                for k in range (i-1):
                    pre = pre.next
                node = pre.next
                aft = node.next
                pre.next = aft
             
        data = node.data
        del node
        self._num_nodes -= 1
        return data
   
    def search(self, target, start=0):
        if self.empty() or start < 0 or start > self._num_nodes - 1:
            raise IndexError("IndexError")
       
        node = self._head
        i = 0
        while i < self._num_nodes:
            if node.data == target and i >= start:
                return target, i
            else:
                i += 1
                node = node.next
       
        return None, -1

    def extend(self, sll):
        if not isinstance(sll, SinglyLinkedList):
            raise TypeError("Type Error")
            
        else:
            for i in range(sll._num_nodes):
                self.insert(self._num_nodes, sll.get(i))
  
