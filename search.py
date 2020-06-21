import requests
import json

def re(url):
    r = requests.get(url)
    r_j = json.loads(r.text)
    return r_j

def search(name):
    url = "https://www.archlinux.org/packages/search/json/?%s=%s"
    n = re(url % ("name", name))
    if len(n["results"]) == 0:
        n2 = re(url %("q", name))
        if len(n2["results"]) == 0:
            raise IndexError("未找到此包")
        else:
            return n2["results"]
    return n["results"]
