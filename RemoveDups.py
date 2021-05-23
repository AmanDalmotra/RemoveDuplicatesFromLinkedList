from LinkedList import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        newNode = ll.head
        tempSet = set([newNode.value])
        while newNode.next:
            if newNode.next.value in tempSet:
                newNode.next = newNode.next.next
            else:
                tempSet.add(newNode.next.value)
                newNode = newNode.next
        return ll


