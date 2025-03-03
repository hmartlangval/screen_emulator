
import asyncio
import json
import threading
import time
from waitress import serve
from flask import Flask
import websockets

stop_event = threading.Event()
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

def flask_thread_function():
    server = serve(app, host='0.0.0.0', port=5000, threads=1, _quiet=True)
    print("Flask thread started @ http://localhost:5000")

    while not stop_event.is_set():
        time.sleep(0.1)  # Important: Check the stop event periodically
    
    server.close()
    print("Flask thread stopped.")

async def websocket_server():
    async with websockets.serve(handler, "localhost", 8765): # Using 'async with' is very important for proper cleanup
        print("WebSocket server started @ ws://localhost:8765")
        while not stop_event.is_set():
            await asyncio.sleep(0.1) # Check stop event periodically
        print("WebSocket server stopped.")

async def handler(websocket):

    # on new connection
    await websocket.send(json.dumps({"message": "WELCOME TO WEBSOCKET"}))

    while True:
        try:
            message = await websocket.recv()
            print(f"Received: {message}")
            await websocket.send(f"Echo: {message}")  # Echo back the message
        except websockets.exceptions.ConnectionClosedOK: # Handle client disconnections gracefully
            break
        except Exception as e:
            print(f"WebSocket error: {e}")
            break

def run_asyncio_loop():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # Fix for windows
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(websocket_server())
    finally:
        loop.close()

def main():
    print('welcome to app')

    flask_thread = threading.Thread(target=flask_thread_function)
    flask_thread.daemon = True
    flask_thread.start()

    websocket_thread = threading.Thread(target=run_asyncio_loop)
    websocket_thread.daemon = True
    websocket_thread.start()


    while True:
        choice = input("Type x to quit (Flask runs in background): ")

        if choice == 'x':
            stop_event.set()
            print("Signaled Flask thread to stop. It will exit when ready.") # Informative message
            break

if __name__ == "__main__":
    main()