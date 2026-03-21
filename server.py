from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()

            if "bye" in data or "quit" in data:
                await websocket.send_text("Goodbye!")
                await websocket.close(code=1000, reason="Client requested close")
                break
            
            await websocket.send_text(f"Message received: {data}")

    except WebSocketDisconnect:
        print(f"WebSocket disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)