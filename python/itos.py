import json
import urllib.request
from optparse import OptionParser

VERSION = 0.1
# Exit codes
STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage, version="%prog" + str(VERSION))
    #parser.add_option("-V","--version", help="Print the version number.")
    parser.add_option("-?" )
    parser.add_option("-w", "--warning", help="Set up the warning treshold.", default=70)
    parser.add_option("-c", "--critical", help="Set up the critical treshold.", default=80)
    parser.add_option("-H", "--hostname", help="Connect to the specified HOSTNAME.", metavar="HOSTNAME",default="localhost")
    parser.add_option("-s", "--size", help="List specific gear size only.")
    parser.add_option("-a", "--all", help="List all gear sizes.")

    (options, args) = parser.parse_args()
    req = urllib.request.Request('http://' + options.hostname + ':8080/admin-console/capacity/profiles.json')
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.readall().decode('utf-8'))
    for r in result:
        print("" + str(result[r]["profile"]) + ": " + str(result[r]["avg_active_usage_pct"]))

if __name__ == "__main__":
    main()
