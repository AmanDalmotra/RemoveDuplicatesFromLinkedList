from LinkedList import LinkedList

def removeDups1(ll):
    if ll.head is None:
        return

    currNode=ll.head
    while currNode:
           runner=currNode
           while runner.next:
                if runner.next.value==currNode.value:
                    runner.next=runner.next.next

                else:
                     runner=runner.next
           currNode=currNode.next


    return currNode

7814789976-nikhil

