from __future__ import print_function

import os.path
import google.auth

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def setValueSheet(value): 
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1H91SiIQiUt1WntgmTOP3hazStHMmqlrHfEdxZjtmDdk'
    SAMPLE_RANGE_NAME = 'import_RaidHelper!B1'
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

        
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:          
        service = build('sheets', 'v4', credentials=creds)
        value_input_option = "RAW"
        values = [[str(value)]]
        body={
                "values": values
            }
        result = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, valueInputOption=value_input_option, body=body).execute()
        print('{0} cells updated.'.format(result.get('updatedCells')))


        """Runs the sample.
        """
        # pylint: disable=maybe-no-member
        script_id = '1_bk9mQoP6EjNPIvjI52W5jlIWYed-Og5PeHVspzCbQFby1m6PjnnmtOP'

        if os.path.exists('token.json'):
            credsApp = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not credsApp or not credsApp.valid:
            if credsApp and credsApp.expired and credsApp.refresh_token:
                credsApp.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials_app.json', SCOPES)
                credsApp = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as tokenApp:
                tokenApp.write(credsApp.to_json())

        #credsApp, _ = google.auth.default()
        serviceApp = build('script', 'v1', credentials=credsApp)

        # Create an execution request object.
        requestApp = {"function": "dataRaid"}

        try:
            # Make the API request.
            responseApp = serviceApp.scripts().run(scriptId=script_id,
                                             body=requestApp).execute()
            if 'error' in responseApp:
                # The API executed, but the script returned an error.
                # Extract the first (and only) set of error details. The values of
                # this object are the script's 'errorMessage' and 'errorType', and
                # a list of stack trace elements.
                error = responseApp['error']['details'][0]
                print(f"Script error message: {0}.{format(error['errorMessage'])}")

                if 'scriptStackTraceElements' in error:
                    # There may not be a stacktrace if the script didn't start
                    # executing.
                    print("Script error stacktrace:")
                    for trace in error['scriptStackTraceElements']:
                        print(f"\t{0}: {1}."
                              f"{format(trace['function'], trace['lineNumber'])}")
            else:
                # The structure of the result depends upon what the Apps Script
                # function returns. Here, the function returns an Apps Script
                # Object with String keys and values, and so the result is
                # treated as a Python dictionary (folder_set).
                folder_set = responseApp['response'].get('result', {})
                if not folder_set:
                    print('No folders returned!')
                else:
                    print('Folders under your root folder:')
                    for (folder_id, folder) in folder_set.items():
                        print(f"\t{0} ({1}).{format(folder, folder_id)}")

        except HttpError as error:
            # The API encountered a problem before the script started executing.
            print(f"An error occurred: {error}")
            print(error.content)

    except HttpError as err:
        print(err)


