import websockets
import asyncio
import json

color = {
        "end": "\033[0m",
        "green_write": "\033[1;42m"
        }

async def receive(websocket):
    while True:
        recv_text = json.loads(await websocket.recv())
        message_type = recv_text["type"]
        messageChain = recv_text["messageChain"]
        for i in range(len(messageChain)-1):
            if message_type == "GroupMessage":
                print(color["green_write"]+str(recv_text["messageChain"][i+1])+color["end"])
            else:
                print(recv_text)

async def main(host):
    async with websockets.connect(host) as websocket:
        await receive(websocket)
