#! /usr/bin/env python
#
#   script generator for project="2021-S1-US-3"
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy + '/lmtoy')
    import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-MX-46"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['G09-44907'] = [ 104042, 104043, 104044, 104046, 104047,     # jan 26
                    104048, 104050, 104051, 104052, 104055,
                    104056, 104057, 104059, 104060, 104061,
                    104063, 104064, 104065,
                    104143, 104144, 104145, 104147, 104148,     # jan 27
                    104149, 104151, 104152, 104153, 104168,
                    104169, 104170, 104172, 104173, 104174,
                    104176, 104177, 104178]
                    
on['G12-42911'] = [ 104100, 104101, 104102, 104104, 104105, 104106,    # jan 26
                    104225, 104226, 104227, 104229, 104230, 104231,    # jan 27
                    104401, 104402, 104403,                            # jan 31 (power failure)
                    104459, 104460, 104461, 104463, 104464, 104465,
                    104467, 104468, 104469, 104487, 104488, 104489,
                    104491, 104492, 104493, 104495, 104496, 104497,
                    104500, 104501, 104502]                            # feb 2


on['NGP-78659'] = [ 104506, 104507, 104508]                            # feb 2

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['G09-44907']   = ""
pars1['G12-42911']   = ""
pars1['NGP-78659']   = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['G09-44907']   = "srdp=1 admit=0"
pars2['G12-42911']   = "srdp=1 admit=0"
pars2['NGP-78659']   = "srdp=1 admit=0"

runs.mk_runs(project, on, pars1, pars2)
