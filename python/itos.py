import json
import urllib.request
req = urllib.request.Request('http://localhost:8080/admin-console/capacity/profiles.json')
with urllib.request.urlopen(req) as response:
    result = json.loads(response.readall().decode('utf-8'))
for r in result:
    print("" + str(result[r]["profile"]) + ": " + str(result[r]["avg_active_usage_pct"]))
