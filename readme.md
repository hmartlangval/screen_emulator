# What is in this project
1. A flask server that can be used to control a web browser
2. A websocket server that can be used to send messages to the flask server
3. A python script that can be used to control the web browser
4. A python script that can be used to analyze the screen of the web browser

# BUILD
```
pyinstaller --onefile --add-data "static;static" --add-data "templates;templates" --name "AIDOEmulator" main.py
```
**--onefile** means to create a single executable file
**--add-data "static;static"** means to add the static folder of source and copy to static
**--add-data "templates;templates"** means to copy templates folder to templates folder