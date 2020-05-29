from mirai import Mirai
from core.config import JsonEvents

cfg = JsonEvents("../cfg.json")
host = cfg.read("host") + "/"
authKey = cfg.read("authKey")
qq = cfg.read("qq")

if cfg.read("socket"):
    app = Mirai(f"mirai://{host}?authKey={authKey}&qq={qq}", websocket=True)
else:
    app = Mirai(f"mirai://{host}?authKey={authKey}&qq={qq}")
