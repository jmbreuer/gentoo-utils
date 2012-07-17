'''
Created on Jul 17, 2012

@author: jmbreuer
'''

from mdaz import SandboxLog
from mdaz.AccessFiles import AccessFiles

if __name__ == '__main__':
    log = file('/tmp/sandbox-debug-6261.log')
    for block in AccessFiles(SandboxLog.process(log)).value():
        print block
