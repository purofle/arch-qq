#!/bin/env python3
from mirai import Mirai, Plain, MessageChain, Group, Member, GroupMessage, At, Source, Plain
from string import Template
import asyncio
from search import *

tmp = '仓库：%s\
\n包名：%s\
\n版本：%s\
\n描述：%s\
\n更新时间：%s\
\n链接：%s'
qq = 3552600542
authKey = '1234567890'

app = Mirai(f"mirai://localhost:8080/?authKey={authKey}&qq={qq}", websocket=True)
@app.receiver("GroupMessage")
async def Main(app: Mirai, group: Group, member: Member, message: MessageChain,source: Source):
    m_id = message.getSource()
    m_text = message.toString()
    if m_text.startswith("pkg"):
        if m_text == "pkg":
            await app.sendGroupMessage(group, [Plain(text="使用pkg+空格+包名来使用！")])
            raise IndexError(message.toString())
        try:
            await app.sendGroupMessage(group, [Plain(text="正在搜索...请稍后...")])
            nn = await search(m_text[4:])
        except IndexError:
            await app.sendGroupMessage(group, [Plain(text="未找到此包！")])
        else:
            nnn = len(nn)
            if nnn > 2:
                nnnn = ""
                for i in range(len(nn)):
                    nnnn += nn[i]["pkgname"] + "\n"
                await app.sendGroupMessage(group, [Plain(text="搜索到了多个包：\n%s" % nnnn)])
            else:
                text = tmp % (nn[0]["repo"],nn[0]["pkgname"],nn[0]["pkgver"],nn[0]["pkgdesc"],nn[0]["last_update"],nn[0]["url"])
                await app.sendGroupMessage(group, [Plain(text=text)])

if __name__ == "__main__":
    app.run()
