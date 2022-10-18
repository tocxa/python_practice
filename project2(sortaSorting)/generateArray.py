import random

arrayList = []                                                                  # Variables declaration
lowBorder = int(input("Type in lowest possible number in array (int)   "))      # and user input for generating an
highBorder = int(input("Type in highest possible number in array (int)   "))    # array or random int numbers
arrayLength = int(input("Type in array length (int)   "))


def generate(low, high, length):             # Array generation function
    file = open('array.txt', 'w')            # Writes array directly to text file
    for i in range(0, length):
        num = random.randint(low, high)
        arrayList.append(num)
        print(num, file=file)
    file.close()


generate(lowBorder, highBorder, arrayLength)

print("\n Your array is:")
print(arrayList)
