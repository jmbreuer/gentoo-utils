'''
Created on Jul 17, 2012

@author: jmbreuer
'''

import pprint

class AccessFiles(object):
    '''
    List of files accessed (without duplicates)
    '''
    def __init__(self, logBlocks, excludeDir = None):
        self.__files__ = set()

        for b in logBlocks:
            if b == None:
                continue
            if b.function == 'open_rd':
                f = b.canonical
                if not f:
                    f = b.absolute
                if not f:
                    continue
                if excludeDir:
                    if f.startswith(excludeDir):
                        continue
                self.__files__.add(f)
    
    def value(self):
        return self.__files__
    
    def __repr__(self):
        return pprint.pformat(self.__files__)
