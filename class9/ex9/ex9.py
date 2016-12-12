#!/usr/bin/env python

from mytest import *

def main():

    print '*' * 50
    print 'Exercise 9a'
    print
    print 'test for func1'
    func1()
    print
    print 'test for func2'
    func2()
    print
    print 'test for func3'
    func3()
    print
    print '*' * 50


    print 'Exercise 9b'
    print
    my_xmas = MyClass('Santa', 'coal', 'Christmas')
    print 'test MyClass.hello'
    my_xmas.hello()
    print
    print 'test MyClass.not_hello'
    my_xmas.not_hello()
    print
    print "That's all folks!"
    print '*' * 50

if __name__ == "__main__":
    main()
