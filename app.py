from flask import Flask, request, jsonify
from drive_utils import list_files, delete_file, move_file, summarize_folder
import logging

app = Flask(__name__)

# Enable debug logging
logging.basicConfig(level=logging.INFO)

# Homepage route to verify server is running
@app.route("/", methods=["GET"])
def home():
    return "WhatsApp Google Drive Assistant is running! Use /webhook for WhatsApp messages."


# Webhook route for Twilio
@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()
    logging.info(f"Received message: {incoming_msg}")

    # Parse command
    if incoming_msg.upper().startswith("LIST"):
        folder = incoming_msg[5:]
        logging.info(f"LIST command for folder: {folder}")
        return respond(list_files(folder))

    elif incoming_msg.upper().startswith("DELETE"):
        path = incoming_msg[7:]
        logging.info(f"DELETE command for file: {path}")
        return respond(delete_file(path))

    elif incoming_msg.upper().startswith("MOVE"):
        try:
            src, dest = incoming_msg[5:].split(" ", 1)
            logging.info(f"MOVE command - file: {src}, destination: {dest}")
            return respond(move_file(src, dest))
        except ValueError:
            return respond("Usage: MOVE <source_file> <destination_folder>")

    elif incoming_msg.upper().startswith("SUMMARY"):
        folder = incoming_msg[8:]
        logging.info(f"SUMMARY command for folder: {folder}")
        return respond(summarize_folder(folder))

    else:
        return respond("Unknown command. Use LIST, DELETE, MOVE, or SUMMARY.")


def respond(message):
    """Format Twilio response (simple text)"""
    from twilio.twiml.messaging_response import MessagingResponse
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
