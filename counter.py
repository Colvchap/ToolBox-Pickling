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
    # Test if the file needs to be read
    if exists(file_name) is False or reset is True:
        fout = open(file_name, 'wb')    # opening a writing file
        counter = 1
        pickle.dump(counter, fout)     # storing counter as bits in file_name
        return counter

        # Read and write to the file
    else:
        fin = open(file_name, 'rb')     # opening a reading file
        counter = pickle.load(fin)
        counter += 1                    # Increasing counter by 1
        finw = open(file_name, 'wb')    # opening a writing file
        pickle.dump(counter, finw)
    fin.close()                         # clean up
    finw.close()
    return(counter)




if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod(verbose=True)
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
