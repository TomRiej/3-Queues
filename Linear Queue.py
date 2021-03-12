# Tom Rietjens
# Linear Queue

OPTIONS = [1,2,3,4,5,6]

class LinearQueue:
    def __init__(self, maxSize=10):
        self.__maxSize = maxSize
        self.__headPointer = 0
        self.__tailPointer = 0
        self.__queue = [None for i in range(self.__maxSize)]

    def add(self, value):
        if not self.full():
            self.__queue[self.__tailPointer] = value
            self.__tailPointer += 1
        else:
            print("queue full...")


    def remove(self):
        if not self.empty():
            self.__headPointer += 1
            print("removed")
        else:
            print("the queue is empty")

    def empty(self):
        if self.__headPointer == self.__tailPointer:
            return True
        else:
            return False

    def full(self):
        if self.__headPointer == 0 and self.__tailPointer == self.__maxSize:
            return True
        else:
            return False


    def printQueue(self):
        for i in range(self.__headPointer,self.__tailPointer):
            print(self.__queue[i])

def menu():
    print("1: Add")
    print("2: Remove")
    print("3. Empty?")
    print("4. Full?")
    print("5. Print queue")
    print("6. Quit")
    valid = False
    while not valid:
        try:
            opt = int(input("what option "))
            if opt in OPTIONS:
                valid = True
                return opt
            else:
                print("invalid")
        except:
            print("not int")

def main():
    """Main procedure,  everything runs through here
    """
    valid = False
    while not valid:
        try:
            size = int(input("what size do you want your queue to be: "))
            valid = True
        except:
            print("not a valid size: int\n")

    myQ = LinearQueue(size)
    
    go = True
    while go:
        option = menu()
        if option == 1:
            val = input("What do you want to add? ")
            myQ.add(val)
        elif option == 2:
            pass
        elif option == 3:
            print(myQ.empty())
        elif option == 4:
            print(myQ.full())
        elif option == 5:
            myQ.printQueue()
        elif option == 6:
            go = False


if __name__ == "__main__":
    main()