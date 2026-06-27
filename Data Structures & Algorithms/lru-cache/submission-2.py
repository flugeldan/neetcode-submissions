from collections import deque
class TreeNode:
    def __init__(self, val: int, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.nodes = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.nodes[key]
        if not node.prev and node.next:
            temp = self.head.next
            self.head = self.head.next
            node.next = None
            temp.prev = None
            self.tail.next, node.prev = node, self.tail
            self.tail = node
        elif node.prev and node.next: #в случае node.prev and not node.next ничего не меняем ибо он и так в конце
            prev_, next_ = node.prev, node.next
            prev_.next = next_
            next_.prev = prev_
            self.tail.next, node.prev = node, self.tail
            node.next = None
            self.tail = node
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if not self.cache:
            node = TreeNode(key)
            self.nodes[key] = node
            self.head = self.tail = node
            self.cache[key] = value
            return
        if key in self.cache:
            node = self.nodes[key]
            if not node.prev and node.next:
                temp = self.head.next
                self.head = self.head.next
                node.next = None
                temp.prev = None
                self.tail.next, node.prev = node, self.tail
                self.tail = node
            elif node.prev and node.next: 
                prev_, next_ = node.prev, node.next
                prev_.next = next_
                next_.prev = prev_
                self.tail.next, node.prev = node, self.tail
                node.next = None
                self.tail = node
        elif key not in self.cache:
            node = TreeNode(key)
            self.nodes[key] = node
            self.tail.next, node.prev = node, self.tail
            self.tail = node
            if len(self.cache) == self.capacity:
                del self.cache[self.head.val]
                del self.nodes[self.head.val]
                if self.head.next:
                    self.head.next.prev = None
                    self.head = self.head.next
                else:
                    self.head = None
        self.cache[key] = value

    
    




    




        


                    
        






                



        
