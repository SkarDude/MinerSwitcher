import nicehash
import requests

host = 'https://api2.nicehash.com'
organisation_id = 'Enter your organisation id'
key = 'Enter your api key'
secret = 'Enter your secret for api key'
plug1_off_wh = 'IFTT webhook url'
plug1_on_wh = 'IFTT webhook url'

private_api = nicehash.private_api(host, organisation_id, key, secret)

rig = private_api.get_rig("SPACESHIP")
print(rig)

if rig['minerStatus'] == "OFFLINE":
    requests.get(plug1_off_wh)
    requests.get(plug1_on_wh)
