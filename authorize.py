import requests
import json

class Authorize:

    def __init__(self, qq: int, host: str, authKey: str):
        self.qq = qq
        self.host = "http://"+host
        self.authKey = authKey
        self.session = None

    def auth(self):
        data = {
                "authKey": self.authKey
        }
        r = requests.post(self.host+"/auth", data=json.dumps(data))
        r_json = json.loads(r.text)
        if not r_json["code"] == 0:
            print(r_json)
            return 1
        else:
            self.session = r_json["session"]
            return 0

    def verify(self):
        data = {
                "sessionKey": self.session,
                "qq": self.qq
                }
        r = requests.post(self.host+"/verify",data=json.dumps(data))
        r_json = json.loads(r.text)
        if not r_json["code"] == 0:
            print(r_json)
            return 1
        return 0

    def release(self):
        data = {
                "sessionKey": self.session,
                "qq": self.qq
                }
        r = requests.post(self.host+"/release",data=json.dumps(data))
        r_json = json.loads(r.text)
        if not r_json["code"] == 0:
            print(r_json)
            return 1
        else:
            return 0
