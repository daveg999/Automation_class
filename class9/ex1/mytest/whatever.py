def func2():
    print "you are calling func2 from whatever module"


def main():
    print "calling main function from whatever.main"
    print "function name __name__ is calling: {}".format(__name__)

if __name__ == "__main__":
    main()
