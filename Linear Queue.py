# Tom Rietjens
# Linear Queue

class LinearQueue:
    def __init__(self, maxSize=10):
        self.__maxSize = maxSize
        self.__headPointer = 0
        self.__tailPointer = 0
        self.__queue = [None for i in range(self.__maxSize)]

    def add(self, value):
        pass

    def remove(self):
        pass

    def printQueue(self):
        print(self.__queue)


def main():
    myQ = LinearQueue(5)
    

if __name__ == "__main__":
    main()