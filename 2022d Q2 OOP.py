#2022d Allocates 1hr 2min in total
# Took 51min 31sec

# Careful of public and protected (double underscore)

class Character():

  def __init__(self, Name, XCoordinate, YCoordinate):
    self.__Name = Name #STRING
    self.__XCoordinate = XCoordinate #INTEGER
    self.__YCoordinate = YCoordinate #INTEGER

# Getters tend to have no parameter otehr than self
# Remember to return the self. attribute

  def GetName(self):
    return self.__Name

  def GetX(self):
    return self.__XCoordinate

  def GetY(self):
    return self.__YCoordinate

  def ChangePosition(self, XChange, YChange):
    self.__XCoordinate = int(self.__XCoordinate) + XChange
    self.__YCoordinate = int(self.__YCoordinate) + YChange

# Remember to use a counter for incrementing by more than
# the loop e.g. counter = counter + 3
# Remmeber to close the file e.g. file.close()

CharacterArray = []

file = open("Characters.txt", "r")
CharacterArray = file.readlines()

for i in range(len(CharacterArray)):
  CharacterArray[i] = CharacterArray[i].strip()

Characters = [] #CHARACTERS

counter = 0

for a in range(0,10):
  Characters.append(Character(CharacterArray[counter], CharacterArray[counter + 1], CharacterArray[counter + 2]))
  counter = counter + 3
  
file.close()

print(Characters)

print(Characters[0].GetName())

#Q2e Allocated 5 marks (10min  took: 9 min 20sec) 

flag = False

while flag == False:
  UserName = input("Enter Name: ") #Rohan (5) Qui (10)
  for x in range(len(Characters)):
    if Characters[x].GetName() == UserName:
      print("Name found in location:", x + 1)
      index = x
      flag = True

print(index)
print(Characters[index].GetY())

# rememebr to cast the data types as ints if
# needed once imported from text file otherwise
# they will be strings

moves = ['A','W','S','D']

UserInput = input("Enter A, W, S or D.")
while UserInput not in moves:
  UserInput = input("Enter A, W, S or D.")

if UserInput == "A":
  Characters[index].ChangePosition(-1, 0)
elif UserInput == "W":
  Characters[index].ChangePosition(0, 1)
elif UserInput == "S":
  Characters[index].ChangePosition(0, -1)
elif UserInput == "D":
  Characters[index].ChangePosition(1, 0)


print(Characters[index].GetY())

print(Characters[index].GetName(), "has changed coordinates to","X = ", Characters[index].GetX(),"and Y =", Characters[index].GetY())


