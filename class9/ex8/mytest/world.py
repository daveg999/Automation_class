def func3():
    print "you are calling func3 from world module"


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

    def __init__(self, why, who, what, when):
        self.why = why
        super(MyChildClass, self).__init__(who, what, when)

    def hello(self):
        print "i want {} to bring {} for my brother at {} because he's in {}".format(self.who, self.what, self.when, self.why)



def main():
    print "calling main function from world.main"
    print "function name __name__ is calling: {}".format(__name__)

if __name__ == "__main__":
    main()

