file = open("array.txt", "r")  # Reading an array from txt file
unsortedArray = file.read()
unsortedArray = unsortedArray.split()  # This step gets you an array of str elements


def arrayToInt(array):  # Function to convert all array elements to int
    n = len(array)
    for i in range(0, n):
        array[i] = int(array[i])
    return array


unsortedArray = arrayToInt(unsortedArray)  # Converting previously read array to int


def bubbleSort(array):
    n = len(array)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


sortedArray = bubbleSort(unsortedArray)  # Sorting an array

print("Sorted array is:")
print(sortedArray)

file = open('sortedArray.txt', 'w')
print(sortedArray, file=file)
file.close()
