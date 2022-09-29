import random
import sys
import traceback

from log import FileLog

logFile = FileLog()
'''
PLEASE NOTE:
------------
Throughout alibrary.py and blibrary.py we will catch any exceptions
raised by an incorrect implementation of FileLog.  We will print the
stacktrace of that exception to help you debug your code. This is not what
you would do in a real application / logging library!
'''


def giftGenerate(count=1):
    """ Gift Generation.

    Input:
        count: int. Number of gifts.

    Output:
        List object, containing the gifts as string.
    """
    glist = ['kettle', 'bell', 'chicken', 'donut', 'gingerman', \
             'doll', 'figure', 'N\' Switch', 'toy car', \
             'skateboard', 'LEGO set', \
             'crayons', 'Rubik\'s cube', 'toy truck']

    ans = []
    for _ in range(count):
        ans.append(random.choice(glist))

    try:
        logFile.info('Generated ' + str(count) + ' gifts from giftGenerate().')
    except:
        traceback.print_exc(file=sys.stdout)
    return ans


def nameGenerate(count=1):
    """ Name Generation.

    Input:
        count: int. Number of children.

    Output:
        List object, containing the names as string.
    """
    nlist = ['James', 'David', 'Christopher', 'George', 'Ronal', 'John', \
             'Richard', 'Daniel', 'Kenneth', 'Anthon', 'Robert', 'Charles',\
             'Paul', 'Steven', 'Kevi', 'Michael', 'Joseph', 'Mark', 'Edward', \
             'Jaso', 'William', 'Thomas', 'Donald', 'Brian', 'Jeff', \
             'Mary', 'Jennifer', 'Lisa', 'Sandra', 'Michell', 'Patricia',\
             'Maria', 'Nancy', 'Donna', 'Laur', 'Linda', 'Susan', 'Karen',\
             'Carol', 'Sara', 'Barbara', 'Margaret', 'Betty', 'Ruth',\
             'Kimberl', 'Elizabeth', 'Dorothy', 'Helen', 'Sharon', 'Debora']

    ans = []
    for _ in range(count):
        ans.append(random.choice(nlist))

    try:
        logFile.info('Generated ' + str(count) + ' names from nameGenerate().')
    except:
        traceback.print_exc(file=sys.stdout)
    return ans
