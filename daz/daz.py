'''
Created on Jul 17, 2012

@author: jmbreuer
'''

from mdaz import SandboxLog
from mdaz.AccessFiles import AccessFiles
from mdaz.AccessPackages import AccessPackages

if __name__ == '__main__':
    log = file('/tmp/sandbox-debug-6261.log')
    print AccessPackages(AccessFiles(SandboxLog.process(log)).value()).packagemap()
    print '-' * 75
