'''
Write your own version of Filelog here!

The Filelog Class opens up a file and adds log messages within.
Previous log messages, if any, should not be removed. Also, there
can be only one Filelog object at any time of this
program - that is, creating a second Filelog object should return
the exact same instance as the first one. (See testing code below.)

At least three methods are required:
info(msg), warning(msg), and error(msg).
'''


class FileLog():
    # TODO: implement a singleton logging class!!
    pass


'''
The following function serves as a simple test to check
whether the id of multiple instances of Filelog remain
the same.
'''


def file_log_test():
    log = FileLog()
    log.info(f'One CS162 Filelog instance found with id {id(log)}')
    log2 = FileLog()
    log2.info(f'Another CS162 Filelog instance Found with id {id(log2)}.')
    if id(log) != id(log2):
        log.error('The singleton implementation is buggy!')
    else:
        log.info('The singleton implementation works!')


if __name__ == '__main__':
    '''
    STANDALONE TESTING:
    -------------------
    If you want to test this logging implementation separately. (ie. not relying
    on any other libraries) then you can run the following:

        $ python3 log.py

    This will run the file_log_test() code, which will verify whether or not
    you have a successful singleton implementation.
    '''
    file_log_test()
