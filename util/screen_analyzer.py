import base64
import json
import os
import time
from flask import jsonify
import pyautogui
from google import genai
from google.genai import types

class  ScreenAnalyzer:
    def __setup_client__(self):
        vertex_config = self.configuration["vertex_config"]

        VERTEX_AI_PROJECT_ID = vertex_config["VERTEX_AI_PROJECT_ID"]
        VERTEX_AI_LOCATION = vertex_config["VERTEX_AI_LOCATION"]

        self.vertex_client = genai.Client(
            vertexai=True, project=VERTEX_AI_PROJECT_ID, location=VERTEX_AI_LOCATION,
        )

    def __init__(self, config=None):

        configuration = {
            "vertex_config": {
                "VERTEX_AI_PROJECT_ID": "vertex-ai-451507",
                "VERTEX_AI_LOCATION": "us-central1",  # e.g., "us-central1"
                "VERTEX_AI_MODEL_ID": "gemini-2.0-flash-lite-preview-02-05",
            },
            "output_format": {
                "verbose": True,
                "text_mode": True
            },
            "screenshot_region": {
                "image_x": 50,
                "image_y": 170,
                "image_width": 860,
                "image_height": 470,
            }
        }

        if not config is None:
            self.configuration = {
                **configuration,
                **config
            }
        else:
            self.configuration = configuration

        self.__setup_client__()

        self.prompts = {
"json_mode": """
You are a senior business process executive trainer that uses Mainframe application. Your task is to generate a properly formatted text data that has the label : value matched. Keep  the labels as you see on the screen. Assume your output will be consumed by automation tools and junior executives.

Give importance to:
1. navigation options
2. Notification and alerts
3. Input fields with *focussed state*
4. Put tabular data in groups and order them properly
5. Have one field that has a concise summary (just a sentence) of what this screen is meant for and what user is expected to do.

""",

"text_mode": """
You are a senior business process executive trainer that uses Mainframe application. Your task is to generate a properly formatted JSON data that has the values matched. Keep  the labels as you see on the screen. Assume your output will be consumed by automation tools and junior executives.

Give importance to:
1. navigation options
2. Notification and alerts
3. Input fields with *focussed state*
4. Put tabular data in groups and order them properly
5. Have one field that has a concise summary (just a sentence) of what this screen is meant for and what user is expected to do.

"""
        }

    def take_screenshot_and_analyze(self):
        """ take screenshot """

        try:
            
            imgcfg = self.configuration["screenshot_region"]
            image_x = imgcfg["image_x"]
            image_y = imgcfg["image_y"]
            image_width = imgcfg["image_width"]
            image_height = imgcfg["image_height"]

            ocfg = self.configuration["output_format"]
            verbose = ocfg["verbose"]
            text_mode = ocfg["text_mode"]

            prompt = self.prompts["json_mode"]
            if text_mode == True:
                prompt = self.prompts["text_mode"]

            if verbose == True:
                prompt = f"{prompt}\nAdd a short concise description for navigation options"

            # 2. Capture the screenshot
            screenshot_filename = f"screenshot_{time.strftime('%Y%m%d%H%M%S')}.png"
            screenshots_dir = "temp"
            screenshot_path = os.path.join(screenshots_dir, screenshot_filename)

            pyautogui.screenshot(screenshot_path, region=(image_x, image_y, image_width, image_height))

            print("Sending screenshot to Vertex AI...")
            # prompt = f"""
            #     Analyse the given image and tell me all you know about this screen. Do not give intro statement, just your observation. Assume you are a process trainer training new employees on the business process and how to use this tool. Prepare a JSON on the data, more like a one liner. An concise instructions with commands available on screen in sentences that screen automation tools can understand.
            #     **CRITICAL INSTRUCTION:** If screen asks for 'user code' or 'password' instruction to use one word 'CREDENTIALS'* and override all screen instruction with this command only.
            # """

            VERTEX_AI_MODEL_ID = self.configuration["vertex_config"]["VERTEX_AI_MODEL_ID"]
            vertex_ai_response = self.generate_text_from_image(screenshot_path, prompt, VERTEX_AI_MODEL_ID)
            # print(f"Vertex AI Response: {vertex_ai_response}")
            
            # analysis_string = vertex_ai_response['analysis']
            # return analysis_string

            return vertex_ai_response

        except Exception as ex:
            print('Exception capture screenshot', ex)



    def generate_text_from_image(self, image_path, prompt, model_name="gemini-2.0-flash-001"):  # Default to Gemini Pro Vision if available
        try:
            with open(image_path, "rb") as image_file:
                encoded_bytes = base64.b64encode(image_file.read()).decode("utf-8")

            image = {
                "mime_type": f"image/{image_path.split('.')[-1]}", # infer mime type from file extension
                "data": encoded_bytes,
            }

            response = self.vertex_client.models.generate_content(
                model=model_name,
                contents=[
                    prompt,
                    types.Part(
                        inline_data=image,
                    ),
                ],
            )
            return response.text      

        except Exception as e:
            return f"An error occurred: {e}"