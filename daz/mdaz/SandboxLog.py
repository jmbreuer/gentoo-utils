'''
Created on Jul 17, 2012

@author: jmbreuer
'''

import re
import pprint

class SandboxLog(object):
    '''
    Parsed sandbox debug log
    '''
    
    block = re.compile(
                       r'F: (?P<function>.*)'
                       r'|S: (?P<status>.*)'
                       r'|P: (?P<input>.*)'
                       r'|A: (?P<absolute>.*)'
                       r'|R: (?P<canonical>.*)'
                       r'|C: (?P<cmdline>.*)'
                       )
    
    fields = ('function', 'status', 'input', 'absolute', 'canonical', 'cmdline')
    
    def __init__(self):
        self.__dict__ = dict.fromkeys(self.fields)
    
    def parse(self, line):
        m = self.block.match(line)
        if m:
            gd = dict((k, v) for k, v in m.groupdict().items() if v)
            self.__dict__.update(gd)
            
    def __repr__(self):
        return pprint.pformat(self.__dict__)


def process(log):
    l = None
    for line in log:
        if line.startswith('F: '):
            l = SandboxLog()
        
        if not line.strip():
            yield l

        if not l == None:
            l.parse(line)
