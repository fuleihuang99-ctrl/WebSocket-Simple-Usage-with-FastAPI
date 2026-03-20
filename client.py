import asyncio
import websockets

async def send_file():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as ws:
        with open("image.png", "rb") as f:  #open file in binary mode
            file_bytes = f.read()
        await ws.send(file_bytes)  # send bytes
        response = await ws.recv()
        print("Server response:", response)

asyncio.run(send_file())