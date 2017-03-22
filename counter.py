""" A program that stores and updates a counter using a Python pickle file
@author: Colvin Chapman
    """

from os.path import exists
import sys
import pickle


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    if exists(file_name) is False or reset is True:
        fout = open(file_name, 'wb')
        counter = 1
        pickle.dump(counter, fout)
        return counter

    else:
        fin = open(file_name, 'rb')
        counter = pickle.load(fin)
        counter += 1
        finw = open(file_name, 'wb')
        pickle.dump(counter, finw)
    fin.close()
    return(counter)




if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod(verbose=True)
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
