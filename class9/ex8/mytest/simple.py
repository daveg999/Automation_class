def func1():
    print "you are calling func1 from simple module"


def main():
    print "calling main function from simple.main"
    print "function name __name__ is calling: {}".format(__name__)

if __name__ == "__main__":
    main()
