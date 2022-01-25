#starting the node class
class Node(object):
    #constructor method
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    #this defines a method to add nodes
    def append(self, data):
        node = Node(data)

        #if we have no nodes:
        if self.tail == None:
            self.tail = node
        #if we have nodes:
        else:
            current = self.tail

            while current.next:
                current = current.next

            current.next = node

        self.size += 1

    #this method let us know the size:
    def size(self): 
        return str(self.size)


    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val

    #this method delete nodes
    def delete(self, data):
        current = self.tail
        previus = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previus.next = current.next
                    self.size -= 1
                    return current.data

            previus = current
            current = current.next

    #this method searchs for a node
    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found')

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0



























































































