def func3():
    print "you are calling func3 from world module"


def main():
    print "calling main function from world.main"
    print "function name __name__ is calling: {}".format(__name__)

if __name__ == "__main__":
    main()
