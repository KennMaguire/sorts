"""
Kenneth Maguire
SelectionSort.py
Interpretted by: Python 3.7.0
Testing with Git

Note: For comparisons, make a function so that it compares and adds to the counter
"""

import header




def selectionSort(unsortedList, _comp):
    exchangeCounter = 0
    nCounter = 0;
    plotArrays = header.plotCandE()
    print(unsortedList)
    for j in range (0,len(unsortedList)):                                     # iterate through array starting at first element (with inner loop finding )
        nCounter += 1
        header.plotCompAndExchange(nCounter, exchangeCounter, _comp.total, plotArrays)
        min = j                                                                 # assume j is min
        for i in range(j+1, (len(unsortedList))):                               # iterate through array from next element (swaps if unsortedList[i] < unsortedList[j])
            if header.comparisonAndCount(unsortedList, min, i, _comp):                            #compare, and if new min found, change min index
                min = i
        if(min != j):
            exchangeCounter += 1                                                #if min is changed to new index point, swap
            unsortedList[j], unsortedList[min] = unsortedList[min], unsortedList[j]
    sortedList = unsortedList                                                   #technically both are now sorted
    print("\nThe length of the sorted list is: " + str(len(sortedList)) + "\n")
    print("The number of array assignments is: " + str(exchangeCounter) + "\n")
    print("The number of comparisons is: " + str(_comp.total) + "\n")

    """The following section is only for plotting the function"""

    header.plt.figure(1)
    header.plt.title("Exchanges for increase in N")
    header.plt.plot(plotArrays.countX, plotArrays.exchY, 'bp-', markersize=5, label='Exchanges')
    header.plt.figure(2)
    header.plt.title("Comparisons for increase in N")
    header.plt.plot(plotArrays.countX, plotArrays.compY, 'yp-', markersize=5, label='Comparisons')
    header.plt.show()

    return(sortedList)

#




print("Please select which file # you'd like to sort \n 1-7")

fileNum = 1     #shuffle.txt
comp = header.comparisonCounter()

testList = []
#inputFile(int(fileNum))
testList = header.inputFile(int(fileNum))
print(testList)
testListSorted = selectionSort(testList, comp)


print(testList)
