'''
Created on Jul 17, 2012

@author: jmbreuer
'''

from collections import defaultdict

class PrettyMap(object):
    '''
    Pretty-print an AccessPackages map
    '''

    def __init__(self, packagemap):
        self.prettymap = defaultdict(list)
        for f, p in packagemap.items():
            self.prettymap[p].append(f)
    
    def printTerse(self):
        for k in self.prettymap:
            print k
    
    def printVerbose(self):
        for k in self.prettymap:
            print k
            for v in self.prettymap[k]:
                print '  ' + v