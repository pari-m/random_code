import csv
import requests

url = 'https://.happyfox.com/api/1.1/json/tickets/'
auth = ('','')
res = requests.get(url,auth=auth)

print(res)