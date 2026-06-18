import os
import gspread

from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from src.llm.prompt_template import STUDENT_ASSISTANT_PROMPT

load_dotenv()

sheet = None

SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

try:

    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials/client_secret.json",
        SCOPES
    )

    creds = flow.run_local_server(port=0)

    client = gspread.authorize(creds)

    spreadsheet = client.open_by_key(
        SHEET_ID
    )

    sheet = spreadsheet.sheet1

    print("Google Sheet Connected Successfully")

except Exception as e:

    print("Google Sheet Error:")
    print(e)

    sheet = None


def get_student_data(student_id):

    if sheet is None:
        return {"error": "Google Sheet not connected"}

    records = sheet.get_all_records()

    for row in records:

        if str(row.get("Student Id")) == str(student_id):
            return row

    return {"error": f"Student {student_id} not found"}