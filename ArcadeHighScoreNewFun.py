name = ""
score = 0
dataArray = []

def ReadFile():
    file = open("HighScoreARC.Txt", "r")
    read = file.read()
    print(read)
    file.close()

def FileToArray():
    file = open("HighScoreARC.Txt", "r")
    count = len(open("HighScoreARC.Txt").readlines())

    for l in range(count):
        mydata = file.readline()
        data = mydata.split(",")
        dataArray.append(data)
        
    print(dataArray)

def DataEntry():
    ScoreInput = False
    while ScoreInput == False:
        print("==========")
        print("Scores range from 1000 - 0.")
        print("==========")
        name = input("Enter 3 digit name.")
        score = int(input("Enter your score."))
        if score >= 1000 and score <= -1:
            print("Your score is invalid.")
        else:
            ("Thank you.")
            dataArray.append([name, score])
            ScoreInput = True

def SortData():
    for i in range(len(dataArray)-1):
        for j in range(0, len(dataArray) - 1):
            dataArray[j+1][1] = int(dataArray[j+1][1])
            dataArray[j][1] = int(dataArray[j][1])
            if dataArray[j][1] < dataArray[j+1][1]:
                tempNum = dataArray[j][1]
                tempName = dataArray[j][0]
                dataArray[j][1] = dataArray[j+1][1]
                dataArray[j][0] = dataArray[j+1][0]
                dataArray[j+1][1] = tempNum
                dataArray[j+1][0] = tempName


    print("Final sort", dataArray)
    

def DataInput():
    fileq = open("SortedARC.Txt", "w")

    b = 0
    for b in range(len(dataArray)):
        fileq.write(str(dataArray[b][0]))
        fileq.write(", ")
        fileq.write(str(dataArray[b][1]))
        fileq.write("\n")

    fileq.close()

ReadFile()

FileToArray()

DataEntry()

SortData()

DataInput()

    
    


    
