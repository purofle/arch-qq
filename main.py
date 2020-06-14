from authorize import Authorize
from config import * 

a = Authorize(qq, host, authKey)
a.auth()
a.verify()
a.release()
