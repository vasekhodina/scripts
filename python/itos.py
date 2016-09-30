import json,sys,urllib.request
from optparse import OptionParser

VERSION = 0.2
# Exit codes
STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

def main():
    return_state = 0 # Set default state to ok
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage, version="%prog" + str(VERSION))
    #parser.add_option("-V","--version", help="Print the version number.")
    parser.add_option("-?" )
    parser.add_option("-w", "--warning", help="Set up the warning treshold.", default=70)
    parser.add_option("-c", "--critical", help="Set up the critical treshold.", default=85)
    parser.add_option("-H", "--hostname", help="Connect to the specified HOSTNAME.", metavar="HOSTNAME",default="localhost")
    parser.add_option("-s", "--size", help="List specific gear size only. Example: int_hosted_small",default="")

    (options, args) = parser.parse_args()

    # Define tresholds
    warn_treshold = options.warning
    crit_treshold = options.critical

    req = urllib.request.Request('http://' + options.hostname + ':8080/admin-console/capacity/profiles.json')
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.readall().decode('utf-8'))
    if not options.size:
        for r in result:
            print("" + str(result[r]["profile"]) + ": " + str(result[r]["avg_active_usage_pct"]))
            if result[r]["avg_active_usage_pct"] > options.warning and return_state < STATE_WARNING:
                return_state = STATE_WARNING
            elif result[r]["avg_active_usage_pct"] > options.critical:
                return_state = STATE_CRITICAL
    else:
        if result[options.size]["avg_active_usage_pct"] > options.warning:
            return_state = STATE_WARNING
            print("WARNING, used gear capacity over " + str(options.warning) + " %!")
        elif result[options.size]["avg_active_usage_pct"] > options.critical:
            return_state = STATE_CRITICAL
            print("CRITICAL, used gear capacity over " + str(options.critical) + " %!")
        else:
            print("OK, used capacity under warning treshold.")
        print("" + str(result[options.size]["profile"]) + ": " + str(result[options.size]["avg_active_usage_pct"]))
    sys.exit(return_state)

if __name__ == "__main__":
    main()
