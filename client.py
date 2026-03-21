import asyncio
import websockets

async def test_client():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as ws:
        await ws.send("Hello, Server!")
        #await ws.send("Quit, Server now!")
        response = await ws.recv()
        print(f"Server response: {response}")

asyncio.run(test_client())