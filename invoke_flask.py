import requests, sys
import json

# newRFP= "http://18.169.62.190:5003/newRFP"
newRFP="http://localhost:5000/newRFP"


clsconf={'rfpid': "rfp1"}
json_string=json.dumps(clsconf)
response = requests.post(newRFP, json=json_string)
myjson=response.json()
print("repsone  after coverting to json", myjson) 