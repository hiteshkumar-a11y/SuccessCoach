import os
import gspread

from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow

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

    spreadsheet = client.open_by_key(SHEET_ID)

    roster_sheet = spreadsheet.worksheet("roster")
    score_sheet = spreadsheet.worksheet("exam_scores")
    attendance_sheet = spreadsheet.worksheet("attendance")
    exam_sheet = spreadsheet.worksheet("exam_schedule")

    print("Google Sheet Connected Successfully")

except Exception as e:
    print("Google Sheet Error:", e)


def get_student_data(student_id):

    student_data = {}

    # Roster
    roster_records = roster_sheet.get_all_records()

    for row in roster_records:
        if row.get("student_id") == student_id:
            student_data["profile"] = row
            break

    # Scores
    score_records = score_sheet.get_all_records()

    student_data["scores"] = [
        row
        for row in score_records
        if row.get("student_id") == student_id
    ]

    # Attendance
    attendance_records = attendance_sheet.get_all_records()

    student_data["attendance"] = [
        row
        for row in attendance_records
        if row.get("student_id") == student_id
    ]

    # Exams
    exam_records = exam_sheet.get_all_records()

    student_data["upcoming_exams"] = [
        row
        for row in exam_records
        if row.get("student_id") == student_id
    ]

    return student_data

def get_student_row(student_id):

    records = sheet.get_all_records()

    for row_index, row in enumerate(records, start=2):

        if str(row.get("Student Id")) == str(student_id):
            return row_index, row

    return None, None

def update_student_field(student_id, column_name, value):

    row_number, student = get_student_row(student_id)

    print("Student:", student)
    print("Row:", row_number)
    print("Column:", column_name)
    print("Value:", value)

    if not student:
        print("Student not found")
        return False

    headers = sheet.row_values(1)

    print("Headers:", headers)

    if column_name not in headers:
        print("Column not found")
        return False

    column_number = headers.index(column_name) + 1

    sheet.update_cell(
        row_number,
        column_number,
        value
    )

    print("Updated successfully")

    return True