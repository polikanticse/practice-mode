import requests

r = requests.get('http://ec2-34-211-79-117.us-west-2.compute.amazonaws.com:8983/solr/admin/metrics?wt=json&type=counter&group=core')
print r.status_code
for i in r.headers:
    print i
print r.encoding
#print r.text
print r.json()

