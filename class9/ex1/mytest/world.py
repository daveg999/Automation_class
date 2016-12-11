def func2():
    print "from world.py, you've called func2!"


def main():
    print "running world.main function as exectuable"
    print "This is the __name__ var: {}".format(__name__)

if __name__ == "__main__":
    main()
