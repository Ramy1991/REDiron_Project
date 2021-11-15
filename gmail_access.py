import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import base64

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_permissions():
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
                r'.\src\Credential.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def get_messages(service):
    # Call the Gmail API, in order to get all messages
    return service.users().messages().list(userId='me').execute()['messages']


def get_message_body(emails, service):
    for email in emails:
        _id = email['id']  # get id of individual message
        message = service.users().messages().get(userId='me', id=_id).execute()  # fetch the message using API
        payload = message['payload']  # get payload of the message
        for item in payload['headers']:
            if item['name'] == 'From' and 'barnesandnoble.com' in item['value']:
                message_body = payload['parts'][0]['body']['data']
                decode_message_body = base64.urlsafe_b64decode(message_body.encode("ASCII")).decode("utf-8")
                # print(message_body)
                return decode_message_body


def main():
    # Checking credentials
    creds = get_permissions()

    # Declare Gmail API service
    service = build('gmail', 'v1', credentials=creds)

    # Get all messages
    emails = get_messages(service)

    email_body = get_message_body(emails, service)
    return email_body


print(main())
