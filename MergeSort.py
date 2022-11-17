import random

def laBurbuja(inputList):
    #A simple bubble sort to compare results with merge sort
    #fun fact: bubble in spanish = burbuja
    for i in range(len(inputList)):
        for j in range(i + 1, len(inputList)):
            if inputList[i] > inputList[j]:
                tmp = inputList[j]
                inputList[j] = inputList[i]
                inputList[i] = tmp

    print(f'BURBUJA RESULT {inputList}')

def merge(a, b):
    """
    Pseudocode for MERGE
    inputs array a and b

    array c

    while (a and b have elements):
        if (a[0] > b[0]):
            add b[0] to the end of c
            remove b[0] from b
        else:
            add a[0] to the end of c
            remove a[0] from a
        |
    at this point either a or b is empty

    while (a has elements):
        add a[0] to the end of c
        remove a[0] from a
    
    while (b has elements):
        add b[0] to the end of c
        remove b[0] from b

    return c
    """

    newList = [0] * (len(a) + len(b))

    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            newList[k] = a[i]
            i += 1
        else:
            newList[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        newList[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        newList[k] = b[j]
        j += 1
        k += 1

    return newList


def mergeSort(inputList):
    """
    pseudocode

    inputs array a
    if (n == 1):
        return a

    a1 = a[0:[n/2]]
    A2 = a[[n/2+1]:n]

    a1 = mergeesort(a1)
    a2 = mergsesort(A2)

    return merge(a1, a2)
    """

    n = len(inputList)

    if (n > 1):
        a1 = inputList[0:(n//2)]
        A2 = inputList[(n//2):n]

        a1 = mergeSort(a1)
        A2 = mergeSort(A2)

        return merge(a1, A2)
    else:
        return inputList


def Main():
    inputList = random.sample(range(100), 10)

    print(f'list: {inputList}')
    laBurbuja(inputList)
    
    outputList = mergeSort(inputList)

    print(outputList)

if __name__ == "__main__":
    Main()