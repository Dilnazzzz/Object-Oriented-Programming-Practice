""" Design Patterns - Singleton and Iterator Example

This is an application to generate Christmas gifts and
distribute them among the children.

Todo:

Write the Filelog function for logging. See log.py for
more info.
"""

from alibrary import giftGenerate, nameGenerate
from blibrary import ChristmasTree

if __name__ == '__main__':
    gift = giftGenerate(count = 8)
    tree = ChristmasTree(gift)

    print('-' * 30)
    tree.decorate()
    tree.show() 

    print('-' * 30)
    kids = nameGenerate(count = 8)
    tree.gift (kids)

    print('-' * 30)
    tree.gift(kids)

    print('-' * 30)
    tree = ChristmasTree(gift)
    try:
        tree.show()
    except:
        pass    

