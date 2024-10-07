class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:

    def __init__(self,start=None):
        self.start = start
        self.item_count = 0

    def is_empty(self):
        return self.start==None
    
    def push(self,data,priority):
        n = Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority<=priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count+=1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count-=1
            return data
    def size(self):
        return self.item_count
    
pq = PriorityQueue()
pq.push(10,0)
pq.push(30,2)
pq.push(20,1)
pq.push(40,3)

while not pq.is_empty():
    print(pq.pop())

        