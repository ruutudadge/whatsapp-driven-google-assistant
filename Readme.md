## WhatsApp-Driven Google Drive Assistant

# ✨ Introduction
Manage your Google Drive directly from WhatsApp with simple text commands!
This project integrates n8n workflows, Twilio WhatsApp API, Google Drive API, and OpenAI GPT to let you:

List files

Delete or move files

Summarize documents (PDF, TXT, DOCX)

Interact in real time via WhatsApp messages

No need to open Google Drive — just chat!

# 🚀 Features
LIST /FolderName → Lists all files in a folder

DELETE /FolderName/FileName → Deletes a file

MOVE /FolderName/FileName /DestinationFolder → Moves a file to another folder

SUMMARY /FolderName → Summarizes documents inside a folder

# 🛠 Tech Stack
Flask (Python) → Webhook and API bridge

n8n → Workflow automation (importable JSON included)

Twilio WhatsApp API → Messaging interface

Google Drive API → File operations

OpenAI GPT → AI-based summarization

ngrok → Local tunnel for webhook testing

# 📂 Project Structure


whatsapp-driven-google-assistant/

│
├── app.py                 
├── drive_utils.py         
├── ai_utils.py             
├── parser.py              
├── log.py                  
├── log_utils.py            
├── requirements.txt        
├── workflow.json          
├── .env.example           
├── .gitignore             
└── README.md               

# ⚡ Setup Guide
1. Clone Repo

git clone https://github.com/<your-username>/whatsapp-driven-google-assistant.git
cd whatsapp-driven-google-assistant

2. Install Dependencies

pip install -r requirements.txt

3. Configure Environment
   
Create .env file from .env.example

Add your Google Service Account JSON filename:

GOOGLE_CLIENT_SECRETS_FILE=whatsapp-drive-assistant-xxxx.json
(Place JSON file in project root, but don’t commit it!)

4. Start Flask Server

python app.py
Visit http://127.0.0.1:5000 — you should see:
“WhatsApp Google Drive Assistant is running!”

5. Expose with ngrok

ngrok http 5000
Copy the public URL shown (e.g., https://abcd1234.ngrok-free.app).

6. Configure Twilio WhatsApp Sandbox

Go to Twilio Console → WhatsApp Sandbox

Set WHEN A MESSAGE COMES IN →


https://abcd1234.ngrok-free.app/webhook
Save.

7. Test Commands
   
Join sandbox (send join <code> to +14155238886), then try:


LIST /ProjectX
SUMMARY /ProjectX
MOVE /ProjectX/report.pdf /Archive
DELETE /ProjectX/notes.txt

# 🎯 Use Cases
Students → Quickly access and organize assignments

Teams → Manage shared project folders remotely

Developers → Example of chat-based cloud automation

# 🔒 Security
Secrets are excluded via .gitignore

Service account JSON must never be committed

Example .env.example is provided for safe sharing

# 🌟 Future Enhancements
Natural Language Commands (e.g., “Move report to archive”)

File upload from WhatsApp

Multi-user access with Google OAuth

Advanced AI summarization options

# 🤝 Contributing
Contributions welcome! Fork this repo, create a branch, and submit a pull request.

# 📜 License
MIT License — free to use, modify, and share.

# Show your support
If you like this project, star the repo ⭐ to show support and inspire more features!
