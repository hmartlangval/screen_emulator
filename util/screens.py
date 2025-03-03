from flask import url_for

from util.mock_emulator_data import switched_off, application_selection, login_prompt, login, main_menu, queues, queue_jobs, claim_detail, claim_detail_update_options
from enum import Enum

class ScreenNames(Enum):
    Off = 99999,
    Start = 0
    MainMenu = 1
    Login = 2
    AccessWorkflow = 3
    # AW_Queue = 31
    AW_Jobs = 33
    AW_Claims_Details = 34
    AW_Claims_Update = 35
    ClaimsEligibility = 4
    ProviderUtility = 5
    GroupMaster = 6
    Authorizations = 7
    Reports = 8
    Print = 9
    ChangeUnderwriter = 10
    LogOff = 11




screens = {
    ScreenNames.Off: {
        "image_url": "off.jpg",
        "navigations": { 
            "START": ScreenNames.Start
        },
        "extra_data": switched_off
    },
    ScreenNames.Start: {
        "image_url": "1-app-selection.jpg",
        "navigations": { 
            "1": ScreenNames.Login, #login
            "9": ScreenNames.Off #logout
        },
        "extra_data": application_selection
    },
    ScreenNames.Login: {
        "image_url": "1.1-user-login.jpg",
        "navigations": {
            "CREDENTIALS": ScreenNames.MainMenu #mainmenu
        },
        "extra_data": login
    },
    ScreenNames.MainMenu: {
        "image_url": "main-menu.jpg",
        "navigations": { 
            "1": ScreenNames.AccessWorkflow,
            # "2": ScreenNames.ClaimsEligibility,
            # "3": ScreenNames.ProviderUtility,
            # "4": ScreenNames.GroupMaster,
            # "5": ScreenNames.Authorizations,
            # "6": ScreenNames.Reports,
            # "7": ScreenNames.Print,
            # "8": ScreenNames.ChangeUnderwriter,
            # "9": ScreenNames.LogOff
        },
        "extra_data": main_menu
        
    },
    
    ScreenNames.AccessWorkflow: {
        "image_url": "queue.jpg",
        "navigations": {
            "1": ScreenNames.AW_Jobs,
            "2": ScreenNames.AW_Jobs,
            "3": ScreenNames.AW_Jobs,
            "4": ScreenNames.AW_Jobs,
            "5": ScreenNames.AW_Jobs,
        },
        "extra_data": queues
    },
    ScreenNames.AW_Jobs: {
        "image_url": "6.1.queue-detail-jobs.jpg",
        "navigations": {
            "A": ScreenNames.AW_Claims_Details,
            "B": ScreenNames.AW_Claims_Details,
            "C": ScreenNames.AW_Claims_Details,
            "D": ScreenNames.AW_Claims_Details,
            "E": ScreenNames.AW_Claims_Details,
            "F": ScreenNames.AW_Claims_Details,
            "G": ScreenNames.AW_Claims_Details,
            "H": ScreenNames.AW_Claims_Details,
            "I": ScreenNames.AW_Claims_Details,
            "J": ScreenNames.AW_Claims_Details,
            "K": ScreenNames.AW_Claims_Details,
            "L": ScreenNames.AW_Claims_Details,
            "M": ScreenNames.AW_Claims_Details,
            "N": ScreenNames.AW_Claims_Details,
            "O": ScreenNames.AW_Claims_Details,
        },
        "extra_data": queue_jobs
    },
    ScreenNames.AW_Claims_Details: {
        "image_url": "claims-details.png",
        "navigations": {
            "O": ScreenNames.AW_Claims_Update
        },
        "extra_data": claim_detail
    },
    ScreenNames.AW_Claims_Update: {
        "image_url": "claim-update-options.jpg",
        "navigations": {
            "Y": "",
            "G": "",
            "J": "",
            "O": "",
            "C": "",
            "S": "",
            "A": "",
            "I": "",
            "E": "",
            "M": "",
            "N": "",
            "X": "",
            "Z": "",
            "H": ""
        },
        "extra_data": claim_detail_update_options
    },
}

class Screens:
    def __init__(self):
        self.current_screen_name = None
        self.current_screen = None
        self.screens = screens

    def getimage(self, filename):
        return { "image_url": self.geturl(filename)}
    
    def geturl(self, filename):
        # with app.app_context():
        # return url_for('static', filename=f'static/screenshots/{filename}')
        return f'static/screenshots/{filename}'

    def is_valid_screen_key(self, key):
        if "navigations" in self.current_screen and key in self.current_screen["navigations"]:
            navs = self.current_screen["navigations"]
            target_screen = navs.get(key)
            return True, target_screen
        
        return False, None


    def serialize_screen(self):

        navigations = None
        if "navigations" in self.current_screen:
            navigations = list(self.current_screen["navigations"].keys())

        return {
            **self.getimage(self.current_screen["image_url"]),
            "navigations": navigations,
            "analysis": self.current_screen["extra_data"]
        }

    def navigate_to(self, screenname):
        if self.screens.get(screenname) is None:
            return self.serialize_screen()
        
        self.current_screen = self.screens.get(screenname)
        self.current_screen_name = screenname
        return self.serialize_screen()


    def handle_input(self, input_str):
        input_str = input_str.upper().strip()

        # if starting the application
        # for any other request if it was not started, return 
        if input_str == "OFF":
            return self.navigate_to(ScreenNames.Off)
        elif input_str == "START" or self.current_screen is None:
            return self.navigate_to(ScreenNames.Start)

        # if self.current_screen is None: #Add this check
        #     return None

        # if "navigations" in self.current_screen and input_str in self.current_screen["navigations"]:
        #     navs = self.current_screen["navigations"]
        #     target_screen = navs.get(input_str)
        #     return self.navigate_to(target_screen)

        is_valid, target_screen = self.is_valid_screen_key(input_str)
        if is_valid == True:
            return self.navigate_to(target_screen)
                
        print("Receipved invalid keystroke: ", input_str)
        return self.serialize_screen()
