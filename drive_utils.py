import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from ai_utils import summarize_text

# Directly specify the JSON file name (put it in same folder)
SERVICE_ACCOUNT_FILE = "whatsapp-drive-assistant-856eca5a30d0.json"  # or "credentials.json"

# Check file existence
if not os.path.exists(SERVICE_ACCOUNT_FILE):
    raise FileNotFoundError(f"Service account file '{SERVICE_ACCOUNT_FILE}' not found. Place it in the project folder.")

# Google Drive API setup
SCOPES = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)


def list_files(folder_name):
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
    results = drive_service.files().list(q=query).execute()
    folders = results.get('files', [])
    if not folders:
        return "Folder not found."
    folder_id = folders[0]['id']

    query = f"'{folder_id}' in parents"
    files = drive_service.files().list(q=query).execute().get('files', [])
    if not files:
        return "No files in folder."
    return "\n".join(f"{f['name']}" for f in files)


def delete_file(file_path):
    file_name = os.path.basename(file_path)
    results = drive_service.files().list(q=f"name='{file_name}'").execute()
    files = results.get('files', [])
    if not files:
        return "File not found."
    drive_service.files().delete(fileId=files[0]['id']).execute()
    return f"Deleted {file_name}."


def move_file(file_path, dest_folder):
    file_name = os.path.basename(file_path)
    file = drive_service.files().list(q=f"name='{file_name}'").execute().get('files', [])
    if not file:
        return "File not found."
    file_id = file[0]['id']

    dest = drive_service.files().list(
        q=f"name='{dest_folder}' and mimeType='application/vnd.google-apps.folder'"
    ).execute().get('files', [])
    if not dest:
        return "Destination folder not found."
    dest_id = dest[0]['id']

    drive_service.files().update(fileId=file_id, addParents=dest_id).execute()
    return f"Moved {file_name} to {dest_folder}."


def summarize_folder(folder_name):
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
    folder = drive_service.files().list(q=query).execute().get('files', [])
    if not folder:
        return "Folder not found."
    folder_id = folder[0]['id']

    query = f"'{folder_id}' in parents"
    files = drive_service.files().list(q=query).execute().get('files', [])
    summaries = []
    for f in files:
        content = drive_service.files().get_media(fileId=f['id']).execute().decode('utf-8', errors='ignore')
        summaries.append(f"{f['name']}:\n{summarize_text(content)}\n")

    return "\n".join(summaries)
