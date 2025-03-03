import asyncio
import base64
import json
import threading
import time
from flask import jsonify
import requests

stop_event = threading.Event()

class EmulatorClient:
    def __init__(self):
        self.REST_API_URL = "http://localhost:5000/command"
        self.REST_API_URL_ANALYSE = "http://localhost:5000/analyse_screen"
        pass

# "A function" that takes input, process it, and gives you back with new set of instructions (screen info and nav options)
    def process_command(self, command):
        try:
            # 1. Call REST API
            print(f"Calling REST API for message: {command}")
            response = requests.post(self.REST_API_URL, json={"message": command})  # Adapt request as needed
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            # rest_response = response.json()  # Parse JSON response
            # print(f"REST API Response: {rest_response}")

            print('SLEEPING 5 seconds before taking screenshot')
            time.sleep(5)
            print('analyzing...')

            try:
                # vertex_ai_response = rest_response.get("analysis")
                vertex_ai_response = requests.post(self.REST_API_URL_ANALYSE)  # Adapt request as needed
                vertex_ai_response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
                vertex_ai_response = response.json()  # Parse JSON response
                try:
                    analysis = vertex_ai_response["analysis"]
                    return analysis
                except Exception as ex2:
                    print("Exception parsing analyze response to JSON", ex2)
                    return vertex_ai_response
            except Exception as ex:
                print('Exception capture screenshot', ex)

        except requests.exceptions.RequestException as e:
            print(f"Error calling REST API: {e}")
            return {"error": str(e)}  # Return error information
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": str(e)}
