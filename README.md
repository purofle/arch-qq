# qq-cli
使用python开发，目前暂时未完善
# 框架
使用[mirai](https://github.com/mamoe/mirai)作为框架
使用[mirai-api-http](https://github.com/mamoe/mirai-api-http)来让python接收到消息
# 依赖
| 依赖 | 作用 |
|:----:|:----:|
|   requests   |   驱动整个项目   |
|   asyncio   |   协程库，驱动websocket来接受消息   |
# 使用
#### 需要先启动`mirai-console和mirai-api-http`！
```bash
git clone https://github.com/purofle/cli-qq
cd cli-qq
pip3 install requests asyncio --user
mv config.py.eg config.py
#自行修改配置文件
python main.py
```
# TODO:
- 发送消息
- 格式化接收到的消息
