import csv
totalWeight=float(0)
with open("HW.csv", newline = '') as data:
    read = csv.reader(data)
    newList = list(read)
    newList.pop(0)

    people = len(newList)



    for weight in newList:

        totalWeight += float(weight[2])
    
    mean = totalWeight/people
    print("The mean is:" + str(mean))

    newList.sort()
    if people % 2:
        median1 = newList[people//2]
        median2 = newList[people//2+1]
        median = (median1+median2)/2 
        print("Median is: " + str(median))
    else:
        median = newList[people//2]
        print("Median is: " + str(median))

    import statistics
    print(statistics.mode(newList))
    
    