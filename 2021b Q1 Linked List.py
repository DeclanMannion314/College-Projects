class node:

  def __init__(self, data, nextNode):
    self.data = data
    self.nextNode = nextNode
    
LinkedList = [node(1, 1), node(5 ,4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56,3), node(0 ,9), node(0, -1)]
startPointer = 0
emptyList = 5

def outputNodes(LinkedList, startPointer):
  while startPointer != -1:
    print(LinkedList[startPointer].data)
    startPointer = LinkedList[startPointer].nextNode

def addNode(LinkedList, startPointer, emptyList):
  UserInput = int(input("Enter data."))
  if emptyList != 9: # while LIST is not full
    ## WHAT IS THIS LOOP DOING? - It gets us the index of the 'last node that points to nothing'
    while LinkedList[startPointer].nextNode != -1: # While the headpointer's next node is not equal to -1
      startPointer = LinkedList[startPointer].nextNode # assigned the nextnode value to the headpointer
    LinkedList[emptyList] = node(UserInput, -1) # added the user input into the list at the next available expty position
    LinkedList[startPointer].nextNode = emptyList # shifted the empty list value to the headpointer's next node value
    #changes the nextNode value of the previously 'last node that points to nothing' to the address/index of the new added node
    return True
    
  else:
    print("False.")
    return False

def delete_node(linkedlist, startpointer):
    emptylist = -1
    value = int(input("enter a number to be removed from the linked list:")) #enters a value to be removed from the linked list
    currentpointer = startpointer
    previous = None


    while currentpointer is not None:
        if linkedlist[currentpointer].data == value:
            break # breaks out of the loop, possibly could change this to a return linkedlist[currentpointer].nextnode
        previous = currentpointer #makes a copy in previous of current pointer because eventually the value of currentpointer will be none
        currentpointer = linkedlist[currentpointer].nextnode    #updates the value of the currentpointer

    if currentpointer is not None:
        if previous is None:
            startpointer = linkedlist[currentpointer].nextnode
       else:
            linkedlist[previous].nextnode = linkedlist[currentpointer].nextnode

        linkedlist[currentpointer].data = None
        linkedlist[currentpointer].nextnode = None
        linkedlist[currentpointer].nextnode = emptylist
        emptylist = currentpointer

        return True

    return False


outputNodes(LinkedList, startPointer)
returnVal = addNode(LinkedList, startPointer, emptyList)
if returnVal == True:
  print("Item added")
else:
  print("Item not added")
outputNodes(LinkedList, startPointer)
 
