from authorize import Authorize
from config import * 
import asyncio
from message.websocket import *

a = Authorize(qq, host, authKey)
a.auth()
a.verify()
session = a.session
print("地址：%s" % host)
try:
    asyncio.get_event_loop().run_until_complete(main(f"ws://{host}/message?sessionKey={session}"))
except KeyboardInterrupt:
    print("释放资源中.....")
    a.release()
    print("释放完毕！已退出！")
