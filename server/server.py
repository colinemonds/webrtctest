#!/usr/bin/env python

import asyncio
from websockets.server import serve
import json

class Server():
    def __init__(self):
        self.server_ips = []

    async def register_server(self, websocket):
        async for message in websocket:
            msg = json.loads(message)
            if msg['server_ip']:
                self.server_ips.append({
                    server_ip: msg['server_ip'],
                    server_port: msg['server_port']
                })
            elif msg['request_server']:
                await websocket.send(self.server_ips)

    async def main(self):
        async with serve(self.register_server, "0.0.0.0", 8765):
            await asyncio.Future()

server = Server()
asyncio.run(server.main())

