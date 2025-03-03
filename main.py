
# This file has 3 systems running all in async thread
# 1. Websocket server
# 2. Flask for REST API
# 3. User Input command

import asyncio
import json
import threading
import time
from waitress import serve
from flask import Flask, jsonify, render_template, request, url_for
import websockets
import requests
from playwright.async_api import async_playwright
import os

from util.screens import Screens
from util.screen_analyzer import ScreenAnalyzer

# since we ran 3 threads, they all listen to this stop_event
# when it is set, they all decided to stop and close their task, graceful shutdown
stop_event = threading.Event()

app = Flask(__name__)
connected_clients = set()
message_queue = asyncio.Queue()  # Use asyncio.Queue for async operations
queue_has_items = asyncio.Event() # Event to signal when the queue is not empty


# # we are using url_for which requires app_context
# # for app_context to work for static a SERVER_NAME needs to be set
# app.config['SERVER_NAME'] = 'localhost:5000'

# # storing a variable for local thread only because wssserver, flask all run in their own thread
# # the variable should be available in their thread
# app_context = threading.local()

SCREENS = Screens()
ANALYZER = ScreenAnalyzer()

## REST API ENDPOINTS
@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/command', methods=['POST'])
def receive_data():
    print('inside /command API endpoint')
    data = request.get_json()
    print(f"Received data from REST API: {data}")

    response = SCREENS.handle_input(data["message"])
    
    _jsonify = jsonify(response)
    message_queue.put_nowait(_jsonify.get_json())
    queue_has_items.set() # Signal that there are items in the queue
    return _jsonify


@app.route('/analyse_screen', methods=['POST'])
def analyze_screen():
    print('inside /analyse_screen API endpoint')
    # data = request.get_json()
    # print(f"Received data from REST API: {data}")

    # response = SCREENS.handle_input(data["message"])
    
    # _jsonify = jsonify(response)

    response = ANALYZER.take_screenshot_and_analyze()
    _jsonify = jsonify(response)
    # message_queue.put_nowait(_jsonify.get_json())
    # queue_has_items.set()
    return _jsonify

## REST API SERVER THREAD - INITIALIZE
def flask_thread_function():
    # global app
    # with app.app_context():
    #     app_context.app = app

    server = serve(app, host='0.0.0.0', port=5000, threads=1, _quiet=True)
    print("Flask thread started @ http://localhost:5000")

    while not stop_event.is_set():
        time.sleep(0.1)  # Important: Check the stop event periodically
    
    server.close()
    
    print("Flask thread stopped.")

## WEBSOCKET SERVER THREAD - INITIALIZE
async def websocket_server():
    async with websockets.serve(handler, "localhost", 8765): # Using 'async with' is very important for proper cleanup
        print("WebSocket server started @ ws://localhost:8765")
        while not stop_event.is_set():
            await asyncio.sleep(0.1) # Check stop event periodically
        print("WebSocket server stopped.")

## WEBSOCKET - EVENT HANDLER
async def handler(websocket):
        
    connected_clients.add(websocket)
    try:
        
        # app_state["current_screen"] = screens.handle_input("start")

        # initial_message = { **app_state["current_screen"]}
        initial = SCREENS.handle_input("off")
        await websocket.send(json.dumps(initial))

        while True:  # Run indefinitely
            message = await websocket.recv() # Wait indefinitely for message
            print(f"Received from WebSocket: {message}")

            # if message.startswith("$sn "):
            #     message = message[2:]
            #     message = message.strip()

            #     print('you asked me to take snapshot and analyze')

            # await websocket.send(json.dumps({ **app_state["current_screen"] })) 
            response = SCREENS.handle_input(message)
            print(response)
            await websocket.send(json.dumps(response)) 

    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket client disconnected.")
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        if websocket in connected_clients:
            connected_clients.remove(websocket)

        # on new connection
        # await websocket.send(json.dumps({"image_url": "static/screenshots/off.jpg"}))
        # using app_context here because we want to use the url_for which needs the app context
        # with app.app_context():
        #     await websocket.send(json.dumps({"image_url": url_for('static', filename=f'screenshots/off.jpg') }))
        # await websocket.send(json.dumps({"image_url": get_image_url('off.jpg') }))

        # while True:
        #     try:
        #         message = await websocket.recv()
        #         print(f"Received: {message}")
        #         await websocket.send(json.dumps(SCREENS.getimage('off.jpg')))
        #     except websockets.exceptions.ConnectionClosedOK: # Handle client disconnections gracefully
        #         break
        #     except Exception as e:
        #         print(f"WebSocket error: {e}")
        #         break

## MESSAGE QUEUE MONITOR AND EVENT HANDLER
async def process_messages_queue():
    while True:
        await queue_has_items.wait()  # Wait for the event to be set
        queue_has_items.clear()      # Reset the event
        while not message_queue.empty(): # Process all messages in queue
            message = message_queue.get_nowait()
            for client in connected_clients:
                try:
                    await client.send(json.dumps(message))
                except Exception as e:
                    print(f"Error sending to client: {e}")
            message_queue.task_done()


## ASYNC IO THREAD - RUNS MULTIPLE THREAD IN ASYNC
def run_asyncio_loop():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # Fix for windows
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        # Create and run both tasks concurrently
        tasks = asyncio.gather(websocket_server(), process_messages_queue())
        loop.run_until_complete(tasks)  # Run both until completion or stop_event is set
    finally:
        loop.close()




browser = None
page1 = None
page2 = None

async def initialize_browser():
    global browser, page1, page2
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page1 = await browser.new_page()
        page2 = await browser.new_page()

        # screen = await page1.viewport_size # Use await
        # screen_width = screen['width']
        # screen_height = screen['height']

        # await page1.set_viewport_size({"width": int(screen_width * 0.6), "height": screen_height})  # Use await
        # await page1.set_position(x=0, y=0) # Use await

        # await page2.set_viewport_size({"width": int(screen_width * 0.6), "height": screen_height})  # Use await
        # await page2.set_position(x=int(screen_width * 0.6), y=0)  # Use await

        # await page1.goto("https://www.google.com") # Use await
        # await page2.goto("https://www.google.co.in") # Use await



def switch_to_tab(tab_index):
    global page1, page2
    if tab_index == 0:
        page1.bring_to_front()
        print("Switched to tab 1")
    elif tab_index == 1:
        page2.bring_to_front()
        print("Switched to tab 2")
    else:
        print("Invalid tab index.")

def close_browser():
    global browser
    if browser:
        browser.close()
        print("Browser closed.")


## MAIN APPLICATION
async def main():

    flask_thread = threading.Thread(target=flask_thread_function)
    flask_thread.daemon = True
    flask_thread.start()

    websocket_thread = threading.Thread(target=run_asyncio_loop)
    websocket_thread.daemon = True
    websocket_thread.start()

    await initialize_browser()

    while True:
        user_input = input("Type x to quit (Flask runs in background): ")

        if user_input == 'x':
            stop_event.set()
            print("Signaled Flask thread to stop. It will exit when ready.") # Informative message
            break

        elif user_input.startswith("w "):
            message = user_input[2:]
            for client in connected_clients:
                await client.send(json.dumps({"message": message}))
                print(f"Sent to websocket clients: {message}")

        elif user_input.startswith("r "):
            message = user_input[2:]
            try:
                response = requests.post('http://localhost:5000/command', json={"message": message})
                print(f"REST API response: {response.json()}")
            except requests.exceptions.RequestException as e:
                print(f"Error sending to REST API: {e}")
        else:
            print(f"Local command: {user_input}")

    if browser:
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())