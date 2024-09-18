class OddLoop:
    def __init__(self, start, stop):
        self.__start = start
        self.__stop = stop

    def print_loop(self):
        for i in range(self.__start, self.__stop + 1):
            if i % 2 != 0:
                print(i, end=" ")


sample = OddLoop(1, 50)
sample.print_loop()
