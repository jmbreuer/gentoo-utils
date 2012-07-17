daz - Dependency AnalyZer
===============================

A tool to analyze portage sandbox debug logs and extract the names of packages read by
the process observed in the sandbox.


Brief HOWTO for observing an ebuild
-----------------------------------

1. Clear out your /var/log/sandbox directory
2. Run emerge like this:

        MAKEOPTS="-j1" SANDBOX_DEBUG=1 emerge -bavt -1 -j1 <atom>

3. Identify the file in /var/log/sandbox corresponding to the build step you're interested in.
<br>For the compile proper, this will usually be the largest.
        
4. Run daz like this (from its gentoo-utils/daz directory as checked out from here):

        python daz.py -X /var/tmp/portage /var/log/sandbox/sandbox-debug-12345.log

You will get two blocks of output, the verbose one on the top and the terse one on the bottom.

The terse output will simply list each package that owns a file that was read by the observed process.

The verbose output will group the actual file names under each package name.
