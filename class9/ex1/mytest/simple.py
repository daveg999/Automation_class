def func1():
    print "from simple.py, you've called func1!"


def main():
    print "running simple.main function as executable"
    print "This is the __name__ var: {}".format(__name__)

if __name__ == "__main__":
    main()
