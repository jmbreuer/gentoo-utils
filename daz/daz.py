'''
Created on Jul 17, 2012

@author: jmbreuer
'''

from mdaz import SandboxLog
from mdaz.AccessFiles import AccessFiles
from mdaz.AccessPackages import AccessPackages
from mdaz.PrettyMap import PrettyMap

from optparse import OptionParser

if __name__ == '__main__':
    op = OptionParser()
    op.add_option("-X", "--exclude-dir", dest="excludeDir", help="exclude directory, files in here are not tracked (i.e. /var/tmp/portage)")
    (options, args) = op.parse_args()
        
    log = file(args[0])
    packages = AccessPackages(AccessFiles(SandboxLog.process(log), options.excludeDir).value())
    '''
    print packages.formatmap()
    print '-' * 75
    '''
    prettyPackages = PrettyMap(packages.packagemap())
    prettyPackages.printVerbose()
    print '-' * 75
    prettyPackages.printTerse()