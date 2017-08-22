import json
from pprint import  pprint
url = "http://ec2-34-211-79-117.us-west-2.compute.amazonaws.com:8983/solr/admin/metrics?wt=json&type=counter&group=core"
import requests
res = requests.get(url)
if res.status_code == 200:
    print "Yes Continuing the work..."
    res_json = res.json()
    #print res_json

for i in res_json["metrics"]["ADMIN./admin/file.requests"]:
    pprint(i)
