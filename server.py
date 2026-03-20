import asyncio # Python's built-in asynchronous I/O library
import websockets # Library for creating WebSocket servers and clients

async def handler(connection):
    print("Client connected")

    message = await connection.recv()
    print("Received from client:", message)
    await connection.send("Hello client!")

async def main():
    async with websockets.serve(handler, "localhost", 8080):
        print("Server started on port 8080")
        await asyncio.Future()

asyncio.run(main())