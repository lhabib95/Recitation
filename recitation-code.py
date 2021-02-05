import csv

def fun1(myName):
    print("My name is " + myName)

def fun2():
    tempList = []
    with open("./recitation_csv.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        for row in csv_reader:
            print(row)
            tempList.append(row)
        for i in range(len(tempList)):
            print(tempList[i][0])

fun1("Luke")
fun2()