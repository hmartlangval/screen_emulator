switched_off = """
            *   The screen displays "Switched OFF".
*   The instruction on the screen is "Send START to switch ON."

```json
{
  "screen_state": "OFF",
  "instructions": "Send START to switch ON"
}
```
        """

application_selection = """
{
  "os_name": "Red Hat Enterprise Linux release 8.5 (Ootpa) (x86_64)",
  "kernel_version": "Linux PPR-ELDHCS01 4.18.0-348.12.2.e18_5.x86_64 x86_64",
  "logged_in_user": "mdoddegowd",
  "application_title": "HCS CORRECTIONAL MANAGEMENT LLC",
  "menu_options": [
    {
      "selection_key": "1",
      "selection_value": "HEALTHpac 4.0 Production"
    },
    {
      "selection_key": "9",
      "selection_value": "Logout"
    }
  ],
  "input_prompt": "Enter selection please >",
  "screen_type": "Menu"
}
"""

login_prompt = "You are a senior business process executive trainer that uses Mainframe application. Your task is to analyse the given screen and generate a properly formatted JSON data (all in first level plain key-value pair). Assume your output will be consumed by automation tools and junior executives. Give importance to navigation options, notification, alerts and currently selected or focussed input fields with one liner tooltip instruction so tools can make proper decision. Put tabular data or list of items in an array of object. Have one field that has a concise summary (just a sentence) of what this screen is meant for and what user is expected to do. Below is the screenshot:"

login="""
{
  "application_title": "Healthpac Systems",
  "company_name": "Eldorado Computing, Inc.",
  "screen_title": "WELCOME",
  "system_name": "Healthpac IV Health Care Management System",
  "company_division": "Health Cost Solutions, Inc. A Division of MPHASIS Inc.",
  "release_version": "4.21.01",
  "login_prompt": "PLEASE LOG INTO THE SYSTEM",
  "login_instructions": "ENTER YOUR USERCODE AND YOUR PASSWORD",
  "username_field_label": "USERCODE",
  "username_field_focus": true,
  "password_field_label": "PASSWORD",
  "copyright_notice": "(c) Copyright 2003 - Eldorado Computing, Inc. All Rights Reserved",
  "notifications": [],
  "alerts": [],
  "input_fields": [
    {
      "field_name": "username",
      "field_type": "text",
      "is_focused": true,
      "data": ""
    },
    {
      "field_name": "password",
      "field_type": "password",
      "is_focused": false,
      "data": ""
    }
  ],
  "navigation_options": []
}
"""

main_menu = """
{
  "application_name": "HEALTHpac",
  "application_version": "4.21.01",
  "screen_title": "HCS CCS Processing",
  "current_date": "Wed Feb 19 2025",
  "current_time": "6:06",
  "user": "MANJUNATHA DODDEGOWD EL",
  "organization": "HCS CORRECTIONAL MGMT WELLPAT",
  "summary": "This is the main menu screen for HCS CCS Processing where users can select various options to manage claims, access workflows, generate reports and other administrative tasks.",
  "menu_options": [
    {
      "option_number": "1",
      "option_text": "ACCESS WORKFLOW"
    },
    {
      "option_number": "2",
      "option_text": "CLAIMS/ELIGIBILITY"
    },
    {
      "option_number": "3",
      "option_text": "PROVIDER UTILITIES"
    },
    {
      "option_number": "4",
      "option_text": "GROUP MASTER"
    },
    {
      "option_number": "5",
      "option_text": "AUTHORIZATIONS"
    },
    {
      "option_number": "6",
      "option_text": "REPORTS"
    },
    {
      "option_number": "7",
      "option_text": "PRINT REPRICING SHEETS (801)"
    },
    {
      "option_number": "8",
      "option_text": "CHANGE UNDERWRITERS"
    },
    {
      "option_number": "9",
      "option_text": "LOG OFF SYSTEM"
    }
  ],
  "input_field_label": "Enter:",
  "input_field": "",
  "input_field_tooltip": "Enter the number corresponding to the desired menu option and press Enter.",
  "navigation_options": {
    "M": "Main Menu",
    "P": "Previous Menu",
    "I": "Information",
    "E": "Electronic Messages"
  },
  "notifications": [],
  "alerts": []
}
"""

queues = """
{
  "screenTitle": "WORKFLOW QUEUES",
  "screenFocus": "***SELECT***",
  "applicationName": "HCS CORRECTIONAL MGMT WELLPATH",
  "userQueuesHeader": "MDODDE'S QUEUES",
  "summary": "This screen displays a list of workflow queues for the user 'MDODDE', allowing the user to select a queue to access its associated jobs. User can use the number 1 to 5, or the arrow up or down keys to navigate.",
  "queueList": [
    {
      "selectionNumber": "1",
      "queueName": "CCH-790136",
      "queueDescription": "PA DOC P1",
      "jobs": "T",
      "isFocussed": true
    },
    {
      "selectionNumber": "2",
      "queueName": "CCH-ARDOC",
      "queueDescription": "ARDOC EFF 1/1/2020 NO BCBS"
    },
    {
      "selectionNumber": "3",
      "queueName": "CCH-CA",
      "queueDescription": "ALL CA SITES HCFA'S"
    },
    {
      "selectionNumber": "4",
      "queueName": "CCH-CA UB",
      "queueDescription": "ALL CA SITES UB'S"
    },
    {
      "selectionNumber": "5",
      "queueName": "CCH-MDCARE",
      "queueDescription": "MEDICARE SITES HCFA AND UBS"
    }
  ],
  "navigationHelp": "Arrow up/down",
  "accessInstruction": "1 Enter to access",
  "footerOptions": {
    "main": "(M)ain",
    "prior": "(P)rior",
    "resume": "(R)esume",
    "detail": "(D)etail",
    "jobCount": "(J)ob count",
    "search": "(S)earch",
    "list": "(L)ist"
  }
}
"""

queue_jobs = """
{
  "screenTitle": "Workflow Queues",
  "applicationTitle": "HCS Correctional Mgmt Wellpath",
  "screenPurpose": "This screen displays a list of workflow queues for the HCS Correctional Management system, allowing the user to select a queue for further action.",
  "instructionBanner": "***SELECT***",
  "columnHeaders": [
    "SEL",
    "ORG DATE",
    "DT TO",
    "Q TIME",
    "TYPE",
    "PA DOC",
    "P1",
    "RECORD DETAIL",
    "EX EX/ TP",
    "PND DUE DT",
    "IMG"
  ],
  "queueItems": [
    {
      "SEL": "A",
      "ORG DATE": "02/11/25",
      "DT TO": "02/19/25",
      "Q TIME": "06:17",
      "TYPE": "CLAIM",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-014871-00",
      "EX EX/ TP": "MCS",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "B",
      "ORG DATE": "02/12/25",
      "DT TO": "02/19/25",
      "Q TIME": "06:17",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015665-00",
      "EX EX/ TP": "BD ZRO",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "C",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015670-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "D",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "224-398127-00",
      "EX EX/ TP": "EP EMM",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "E",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015671-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "F",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015680-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "G",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "224-398139-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "H",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015684-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "I",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015687-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "J",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015690-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "K",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "224-398146-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "L",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "224-398154-00",
      "EX EX/ TP": "EP EMM",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "M",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015704-00",
      "EX EX/ TP": "EP EMM",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "N",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015705-00",
      "EX EX/ TP": "EP EMM",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "O",
      "ORG DATE": "02/12/25",
      "DT TO": "02/13/25",
      "Q TIME": "06:14",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-015706-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    }
  ],
  "inputFieldLabel": "ENTER SELECTION:",
  "inputFieldValue": null,
  "inputFieldTooltip": "Enter the selection code (A-O) corresponding to the desired workflow queue and press Enter.",
  "urgencyNote": "* = Urgent"
}
"""

claim_detail = """
{
  "summary": "This screen displays claim details and allows users to view information such as claim status, charges, payments, patient and provider details.",
  "CLAIM INFORMATION": {
    "TY": "MM",
    "CLAIM NUMBER": "225-014871-00",
    "STATUS OF CLAIM": "ΡΕΝΗ 02/18/25 REUBEN",
    "RECEIVED": "02/11/25",
    "INCURRED": "01/23/25",
    "PLAN ID": "790136A",
    "EFFECTIVE": "02/01/17",
    "DGN": "R06",
    "DESCRIPTION": "Abnormalities o",
    "ICD": "R06.02",
    "YEAR": "2025",
    "UND/GROUP CODES": "790 790136",
    "NETWK": "CMA",
    "CLAIM SOURCE": "EDI 02/12/25"
  },
  "CLAIM DETAILS": [
    {
      "BEN": "780",
      "FROM DOS": "01/23/25",
      "VISIT": "1",
      "CHARGE AMT": "1096.60",
      "DISALLOWED": "578.53",
      "DEDUCTIBLE": ".00",
      "PCT": "100",
      "PAYMENT": "518.07",
      "type": "P"
    },
    {
      "BEN": "780",
      "FROM DOS": "01/23/25",
      "VISIT": "0",
      "CHARGE AMT": "172.32",
      "DISALLOWED": "29.56",
      "DEDUCTIBLE": ".00",
      "PCT": "100",
      "PAYMENT": "142.76",
      "type": "P"
    },
    {
      "BEN": "780",
      "FROM DOS": "01/23/25",
      "VISIT": "0",
      "CHARGE AMT": "40.16",
      "DISALLOWED": "40.16",
      "DEDUCTIBLE": ".00",
      "PCT": "0",
      "PAYMENT": ".00",
      "type": "P"
    },
    {
      "BEN": "780",
      "FROM DOS": "01/23/25",
      "VISIT": "0",
      "CHARGE AMT": "133.91",
      "DISALLOWED": "133.91",
      "DEDUCTIBLE": ".00",
      "PCT": "0",
      "PAYMENT": ".00",
      "type": "P"
    }
  ],
  "TOTALS": {
    "CHARGE AMT": "1442.99",
    "DISALLOWED": "782.16",
    "DEDUCTIBLE": ".00",
    "PAYMENT": "660.83"
  },
  "ADJUSTMENTS": {
    "ADJ": ".00",
    "COB ADJ": ".00",
    "W/HOLD": ".00",
    "TOT": ".00"
  },
  "PARTY INFORMATION": {
    "PATIENT": {
      "TAX ID": "997314611",
      "EMPLOYEE/PATIENT": "WHITE, ALVIN / (Self)"
    },
    "PROVIDER": {
      "TAX ID": "251799853",
      "PROVIDER": "SUPERIOR AMBULANCE SERVICE INC"
    },
    "ALT PAYEE": null,
    "CHECK NO": null,
    "NET PAYMENT": [".00", "660.83", ".00", "660.83"]
  },
  "NAVIGATION": {
    "SELECT": "Choose an option",
    "OPTIONS": [
      "(M)ain",
      "(P)rior",
      "(R)esume",
      "(U)npend",
      "(V)iew",
      "(O)ptions",
      "(F)ind"
    ],
    "focussed": "Y"
  },
  "ALERTS": {
    "IMAGE AVAILABLE": true,
    "E-PAY INFO": "--- >",
    "CLAIM NOTES EXIST": true
  }
}

"""


claim_detail_update_options = """
{
  "screen_summary": "This screen provides a list of options for claim processing, allowing the user to select an action to perform on the claim or navigate to other related functions.",
  "screen_title": "Select Option",
  "navigation_options": [
    {
      "key": "Y",
      "description": "return to summary screen"
    },
    {
      "key": "G",
      "description": "Additional Options"
    },
    {
      "key": "J",
      "description": "re-adjudicate claim"
    },
    {
      "key": "O",
      "description": "Override adjudication results"
    },
    {
      "key": "C",
      "description": "Cancel Adjudication Results"
    },
    {
      "key": "S",
      "description": "Modify Service Line Details"
    },
    {
      "key": "A",
      "description": "Enter Adjustment Dollars"
    },
    {
      "key": "I",
      "description": "Change/add COB Information"
    },
    {
      "key": "E",
      "description": "pEnd the claim"
    },
    {
      "key": "M",
      "description": "Mark claim for payment"
    },
    {
      "key": "N",
      "description": "add or modify claim Notes"
    },
    {
      "key": "X",
      "description": "New Claim - Same Patient"
    },
    {
      "key": "Z",
      "description": "New Claim - New Patient"
    },
    {
      "key": "H",
      "description": "Hold/release claim from payment"
    },
    {
      "key": "T",
      "description": "Transfer workflow job"
    },
    {
      "key": "Q",
      "description": "next workflow Queue job"
    }
  ],
  "input_field": {
    "field_name": "ENTER OPTION",
    "value": "",
    "description": "Input field for the user to enter the option key",
    "focus": true
  },
  "alerts": [
    {
      "message": "IMAGE AVAILABLE",
      "type": "information",
      "description": "Indicates that an image is available for the claim"
    },
    {
      "message": "CLAIM NOTES EXIST",
      "type": "information",
      "description": "Indicates that claim notes exist for the claim"
    }
  ],
  "monetary_value": {
    "value": "0.00",
    "description": "A monetary value displayed on the screen"
  },
    "total_value": {
    "value": "201.66",
    "description": "A total value displayed on the screen"
  }
}
"""








