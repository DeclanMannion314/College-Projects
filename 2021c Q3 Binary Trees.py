ArrayNodes = [[(0) for x in range(3)] for y in range(20)] #ARRAY FOR INT
RootPointer = -1 #INTEGER
FreeNode = 0 #INTEGER

print(ArrayNodes)

def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Ener the data"))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]

        FreeNode = FreeNode + 1
    else:
        print("Tree is full.")

    return ArrayNodes, RootPointer, FreeNode

def PrintAll(ArrayNodes):
    for x in range(0,20):
        print(ArrayNodes[x][0], ArrayNodes[x][1], ArrayNodes[x][2])

for y in range(0,10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)  
print(ArrayNodes)
PrintAll(ArrayNodes)

# print("Root", RootPointer)
# print("Free", FreeNode)

#def InOrder(ArrayNodes, RootPointer):
#  if ArrayNodes[RootPointer][0] != -1:
#    InOrder(ArrayNodes, ArrayNodes[RootPointer][0])
#  print(ArrayNodes[RootPointer][1])
#  if ArrayNodes[RootPointer][2] != -1:
#    InOrder(ArrayNodes, ArrayNodes[RootPointer][2])

#InOrder(ArrayNodes, RootPointer)

#def PostOrder(ArrayNodes, RootPointer):
#   if ArrayNodes[RootPointer][0] != -1:
#     PostOrder(ArrayNodes, ArrayNodes[RootPointer][0]) #1 #9 #
#   if ArrayNodes[RootPointer][2] != -1:
#     PostOrder(ArrayNodes, ArrayNodes[RootPointer][2]) #1 #9 #
#   print(ArrayNodes[RootPointer][1])
      
# print("Post order")   
# PostOrder(ArrayNodes, RootPointer)


def PreOrder(ArrayNodes, RootPointer):
    print(ArrayNodes[RootPointer][1])
    if ArrayNodes[RootPointer][0] != -1:
        PreOrder(ArrayNodes, ArrayNodes[RootPointer][0]) #1 #9 #
    if ArrayNodes[RootPointer][2] != -1:
        PreOrder(ArrayNodes, ArrayNodes[RootPointer][2]) #1 #9 #

print("Pre order")
PreOrder(ArrayNodes, RootPointer)
