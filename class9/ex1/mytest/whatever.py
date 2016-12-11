def func3():
    print "from whatever.py, you've called func3!"


def main():
    print "running whatever.main function as executable"
    print "This is the __name__ var: {}".format(__name__)

if __name__ == "__main__":
    main()
