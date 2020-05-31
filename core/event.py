from mirai import (
    Mirai, Plain, At,
    MemberJoinEvent,
    GroupMessage,
    Group,MessageChain,
    Member
)
from core.config import JsonEvents
import asyncio

cfg = JsonEvents("cfg.json")
host = cfg.read("host") + "/"
authKey = cfg.read("authKey")
qq = cfg.read("qq")

if cfg.read("socket"):
    app = Mirai(f"mirai://{host}?authKey={authKey}&qq={qq}", websocket=True)
else:
    app = Mirai(f"mirai://{host}?authKey={authKey}&qq={qq}")



@app.receiver("MemberJoinEvent")
async def member_join(app: Mirai, event: MemberJoinEvent):
    await app.sendGroupMessage(
        event.member.group.id,
        [
            At(target=event.member.id),
            Plain(text="欢迎进群!")
        ]
    )

@app.receiver("GroupMessage")
async def group_message(app: Mirai, group: Group, member: Member, message: MessageChain):
    print(message.toString())
    if message.toString().startswith("test"):
        await app.sendGroupMessage(
            group,
            [
                Plain(text="test")
            ]
        )


