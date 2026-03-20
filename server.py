import asyncio # Python's built-in asynchronous I/O library
import websockets # Library for creating WebSocket servers and clients

# async def handler(connection):
#     print("Client connected")

#     message = await connection.recv()
#     print("Received from client:", message)
#     await connection.send("Hello client!")

async def file_handler(ws):
    print("Client connected, waiting for file...")
    file_bytes = await ws.recv()  # receive bytes
    with open("received_file.png", "wb") as f:
        f.write(file_bytes)
    print("File received and saved!")
    await ws.send("File received successfully!")

async def main():
    async with websockets.serve(file_handler, "localhost", 8000):
        print("Server running on ws://localhost:8000")
        await asyncio.sleep(50)  # keep server alive

asyncio.run(main())