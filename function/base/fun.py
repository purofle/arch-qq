from mirai import Mirai, Group, Member, MessageChain, At, Plain
import asyncio
import requests

async def yiyan(app: Mirai, group: Group, member: Member,message: MessageChain):
    if message.toString().find("一言") == -1:
        return False


