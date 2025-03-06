# while 
class different_loops:
    def WhileLoop(self ,counter: int = 1 ):

        while counter <= 10:
            print("hello world ", counter)
            counter = counter + 1

    def ForLoop(self, n :int = 1):
        print(f'n = {n}')
        for item in range(n):
            print(item **2 , "is the square of", item)







loop = different_loops()
#loop.WhileLoop(4)
loop.ForLoop(5)