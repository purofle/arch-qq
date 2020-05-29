import os
import json

base_json = {
    "bot": {
        "qq": 123456,
        "host": "127.0.0.1:8080",
        "authKey": "authKey",
        "socket": True
    }
}


class JsonEvents:
    def __init__(self, path):
        self.path = path

    def read(self, block2, block="bot"):
        with open(self.path, "r") as f:
            _f_b = f.read()
        _j = json.loads(_f_b)
        return _j[block][block2]

    if not os.path.exists("cfg.json"):
        print("配置文件不存在,正在创建中....")
        with open("cfg.json", "w") as file:
            file.write(json.dumps(base_json, indent=4))
        exit(1)
