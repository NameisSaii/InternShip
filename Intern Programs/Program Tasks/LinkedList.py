class Node:
    def __init__(self, data):
        self.nextNode = None
        self.data = data

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if(self.head is None):
            self.head = Node(data)
        else:
            # Iterate to last node of linked list
            pointer = self.head
            while(pointer.nextNode is not None):
                pointer = pointer.nextNode
            # Set reference of nextNode pointer of last node to the new node.
            pointer.nextNode = Node(data)

    def delete(self, data):
        pointer = self.head
        while(pointer.nextNode.data!=data):
            pointer = pointer.nextNode
            if(pointer.data!=data and pointer.nextNode is None):
                print(pointer.data)
                return 0
        pointer.nextNode = pointer.nextNode.nextNode

    def traverse(self):
        pointer = self.head
        while(1):
            print(pointer.data, end="")
            if(pointer.nextNode is None):
                print()
                break
            print("", end=" => ")
            pointer = pointer.nextNode

if __name__ == "__main__":
    myList = SinglyLinkedList()

    while(True):
        print("*"*30)
        el = int(input("1 to Insert\n2 To Deletion\n3 TO Search\n4 to exit\n"))
        if(el == 1):
            item = input("Enter Element to insert in Linked List\n")
            myList.insert(item)
        if(el == 2):
            item = input("Enter Element to delete in Linked List\n")
            print("Element not found" if myList.delete(item)==0 else "Deleted")
        if(el == 3):
            myList.traverse()
        if(el == 4):
            break