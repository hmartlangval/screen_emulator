# Steps to run the server
1. ``AIDOEmulator.exe`` is the server service
2. ``Double-click`` and let it run.
3. You can close it by typing ``"x"`` or by closing the command window

# UI view of server
1. Open ``http://localhost:5000``

# Steps to use the emulator from python code
1. Copy the ``emulator_client.py`` file into your project
2. Create a new instance ``client = EmulatorClient()``
3. Call the ``process_command`` like this: ``client.process_command(<command>)``

```
client = EmulatorClient()
client.process_command('start')

client.process_command('1')
client.process_command('off')
client.process_command('credentials')
client.process_command('A')
client.process_command('O')
...
```

**NOTE**: ``process_command`` returns a detailed information of the new screen that is the result of the command that is just sent. Return value could be in string format containg data as in any of the following:
* JSON format
* Text represention
* Combination of both