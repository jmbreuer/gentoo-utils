'''
Created on Jul 17, 2012

@author: jmbreuer
'''

from mdaz import SandboxLog
from mdaz.AccessFiles import AccessFiles
from mdaz.AccessPackages import AccessPackages
from mdaz.PrettyMap import PrettyMap

if __name__ == '__main__':
    log = file('/tmp/sandbox-debug-6261.log')
    packages = AccessPackages(AccessFiles(SandboxLog.process(log)).value())
    '''
    print packages.formatmap()
    print '-' * 75
    '''
    prettyPackages = PrettyMap(packages.packagemap())
    prettyPackages.printVerbose()
    print '-' * 75
    prettyPackages.printTerse()