import json

import requests

class Settings():
    url = "https://app.clockster.com/employees/list?active=true&page=1&search&location_id=1052&department_id=1165&cursor"
    url2 = "https://apis.clockster.com/company/v1/auth/token"
    pamparam = dict(client_id = "769", client_secret = "ZV7dypiRV4RfgjmBQZLfbRjgoUVtUelf1c7xDEQK")
    id = "769"
    secret = "ZV7dypiRV4RfgjmBQZLfbRjgoUVtUelf1c7xDEQK"
get = requests.get(Settings.url2)
post = requests.post(Settings.url2, params=Settings.pamparam)
#t = json.loads(r.text)

print(post.text)