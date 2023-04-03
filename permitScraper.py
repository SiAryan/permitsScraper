"""

Step 1:
- research open data portal vancouver
- locate desired dataset 
    https://opendata.vancouver.ca/explore/dataset/issued-building-permits/information/
- get api 
    https://opendata.vancouver.ca/api/v2/catalog/datasets/issued-building-permits/records?select=%2A&limit=10&offset=0&timezone=UTC


Step 2: 
- search fields
- query data from for loop


"""
import requests
import json
api_url = "https://opendata.vancouver.ca/api/v2/catalog/datasets/issued-building-permits/records?select=%2A&limit=10&offset=0&timezone=UTC"
response = requests.get(api_url)
data = json.loads(response.text)




"""
permitnumber, description, status, applicant name
"""

for i in data["records"]:
    # print(i["record"]["fields"])
    print("--------------------------------------------------------------\n")
    print("PERMIT NUMBER : {pnum}\nDESCRIPTION : {desc}\nAPPLICANT NAME : {a_name}\n".format(pnum = i["record"]["fields"]["permitnumber"], desc = i["record"]["fields"]["projectdescription"], a_name = i["record"]["fields"]["applicant"]))