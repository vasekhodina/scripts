import json
import urllib.request
from optparse import OptionParser

VERSION = 0.1
# Exit codes
STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

usage = "usage: %prog [options] arg1 arg2"
parser = OptionParser(usage=usage, version="%prog" + str(VERSION))
parser.add_option("-V","--version", help="Print the version number.")
parser.add_option("-?" )
parser.add_option("-w", "--warning", help="Set up the warning treshold.")
parser.add_option("-c", "--critical", help="Set up the critical treshold.")
parser.add_option("-H", "--hostname", help="Connect to the specified HOSTNAME.", metavar="HOSTNAME")

# Tresholds
warn_treshold = 70
crit_treshold = 80

req = urllib.request.Request('http://localhost:8080/admin-console/capacity/profiles.json')
with urllib.request.urlopen(req) as response:
    result = json.loads(response.readall().decode('utf-8'))
for r in result:
    print("" + str(result[r]["profile"]) + ": " + str(result[r]["avg_active_usage_pct"]))
