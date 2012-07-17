'''
Created on Jul 17, 2012

@author: jmbreuer
'''

import os
import pprint

class AccessPackages(object):
    '''
    Associate a list of files with the portage packages they belong to
    '''


    def __init__(self, files):
        pkgcache = dict()
        self.packages = dict()
        
        for f in files:
            if not pkgcache.has_key(f):
                self.populate(pkgcache, f)
            if not pkgcache.has_key(f):
                self.packages[f] = 'UNKNOWN'
            else:
                self.packages[f] = pkgcache[f]

    def packagemap(self):
        return self.packages

    def formatmap(self):
        return pprint.pformat(self.packages)

    def populate(self, pkgcache, f):
        package = os.popen('qfile -C -e ' + f).readline()
        if not package.split():
            pkgcache[f] = 'NONE'
            return
        package = package.split()[0]
        
        pfiles = os.popen('qlist -C ' + package)
        for pfile in pfiles:
            pkgcache[pfile.strip()] = package
