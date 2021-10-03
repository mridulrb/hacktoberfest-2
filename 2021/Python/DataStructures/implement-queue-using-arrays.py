# Queue is a FIFO - First in First Out data structure

class Queue:
    # To initialize the object.
    def __init__(self, c):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c
 
    # Function to insert an element at the rear of the queue
    def EnQueue(self, data):
        # Check queue is full or not
        if(self.capacity == self.rear):
            print("\nQueue is full")
 
        # Insert element at the rear
        else:
            self.queue.append(data)
            self.rear += 1
 
    # Function to delete an element from the front of the queue
    def DeQueue(self):
        # If queue is empty
        if(self.front == self.rear):
            print("Queue is empty")
 
        # Pop the front element from list
        else:
            x = self.queue.pop(0)
            self.rear -= 1
 
    # Function to print queue elements
    def printQueue(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
 
        # Traverse front to rear to print elements
        for i in self.queue:
            print(i, "<--", end = '')
     
    # Print front of queue
    def Front(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
 
        print("\nFront Element is:", self.queue[self.front])
 
# Driver code
if __name__=='__main__':
    # Create a new queue of capacity 4
    q = Queue(4)
 
    # Print queue elements
    q.printQueue()
 
    # Inserting elements in the queue
    q.EnQueue(20)
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
 
    # Print queue elements
    q.printQueue()
 
    # Insert element in queue
    q.EnQueue(60)
 
    # Print queue elements
    q.printQueue()
    
    # Delete queue elements
    q.DeQueue()
    q.DeQueue()
    print("\n\nafter two node deletion\n")
 
    # Print queue elements
    q.printQueue()
 
    # Print front of queue
    q.Front()
