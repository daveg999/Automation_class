def func3():
    print "you are calling func3 from world module"

''' add a child class '''

class MyClass(object):

    def __init__(self, who, what, when):
        self.who = who
        self.what = what
        self.when = when

    def hello(self):
        print "if you are good, {} will bring presents instead of {} for {}".format(self.who, self.what, self.when)


    def not_hello(self):
        print "my performance review says i'm getting {} from {} for sure this {}".format(self.what, self.who, self.when)

class MyChildClass(MyClass):

    def hello(self):
        print "i want {} to bring {} for my brother at {}".format(self.who, self.what, self.when)



def main():
    print "calling main function from world.main"
    print "function name __name__ is calling: {}".format(__name__)

if __name__ == "__main__":
    main()

    ''' validation test '''
    my_xmas = MyClass("Santa Claus", "lumps of coal", "Christmas")
    print
    print my_xmas.who
    print my_xmas.what
    print my_xmas.when
    print
    my_xmas.hello()
    print
    my_xmas.not_hello()
    print
    my_bros_xmas = MyChildClass("Santa Claus", "lumps of coal", "Christmas")
    print
    my_bros_xmas.hello()
    print
    my_bros_xmas.not_hello()
    print
