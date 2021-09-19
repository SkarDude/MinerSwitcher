import nicehash
import requests


private_api = nicehash.private_api(host, organisation_id, key, secret)

rig = private_api.get_rig("SPACESHIP")
print(rig)

if rig['minerStatus'] == "OFFLINE":
    requests.get(plug1_off_wh)
    requests.get(plug1_on_wh)
